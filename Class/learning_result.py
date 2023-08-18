import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np


class LearningResult:

    def __init__(self, pipeline, x, y, x_treino, y_teste, y_pred, y_pred_test):
        self.pipeline = pipeline
        self.x = x
        self.y = y
        self.X_treino = x_treino
        self.y_teste = y_teste
        self.y_pred = y_pred
        self.y_pred_test = y_pred_test
        self.plt = None
        self.fig = None
        self.metrics_names = None
        self.n_folders = None
        self.cross_val = None
        self.datas_cv = None
        self.k = None
        self.accuracies = None
        self.conf_mat = None
        self.ranking_report = None
        #defini manualmente, depois, corrigir
        self.class_one = '0'
        self.class_two = '1'

    def get_class_names_in_classification_column(self):
        #aqui, buscar quais os valores na coluna de rótulos, para definir class_one e class_two
        pass

    def plot_tree(self):
        self.fig = plt.figure(figsize=(25, 9), dpi=600)
        _ = tree.plot_tree(self.pipeline.named_steps['Decisiontree'],
                           feature_names=self.X_treino,
                           class_names=[self.class_one, self.class_two],
                           filled=True)
        self.fig.savefig("decistion_tree.png")

    def cross_validate_m(self, cv):
        self.metrics_names = ['accuracy', 'precision_macro', 'recall_macro']
        metrics = cross_validate(self.pipeline, self.x, self.y, cv=cv, scoring=self.metrics_names)
        print("Cross Validate:\n")
        for met in metrics:
            print(f"- {met}:")
            print(f"-- {metrics[met]}")
            print(f"-- {np.mean(metrics[met])} +- {np.std(metrics[met])}\n")

    def k_fold_m(self, k, n_folders):
        n_folders = n_folders
        cross_val = KFold(n_splits=n_folders, shuffle=True, random_state=32)
        self.datas_cv = {f"folder_{f + 1}": {"treino": None, "teste": None} for f in range(n_folders)}
        k = k
        for indices_treino, indices_teste in cross_val.split(self.x):
            self.datas_cv[f"folder_{k}"]["treino"] = (self.x.values[indices_treino], self.y.values[indices_treino])
            self.datas_cv[f"folder_{k}"]["teste"] = (self.x.values[indices_teste], self.y.values[indices_teste])
            k += 1
        print("K-Fold Cross Validate:\n")
        print(self.datas_cv.keys())

    def show_k_fold_m_accuracies(self):
        acuracias = list()
        for folder in self.datas_cv:
            self.pipeline.fit(self.datas_cv[folder]["treino"][0], self.datas_cv[folder]["treino"][1])
            ac_i = self.pipeline.score(self.datas_cv[folder]["teste"][0], self.datas_cv[folder]["teste"][1])
            acuracias.append(ac_i)
            print(f"{folder}: {ac_i}")

        print("\n- Acurácia das folders:")
        print(f"Media: {round(np.mean(acuracias) * 100, 2)}%")
        print(f"Desvio padrão: {round(np.std(acuracias) * 100, 2)}%")

    def show_classification_report(self):
        report = classification_report(self.y_teste, self.y_pred_test, target_names=[self.class_one, self.class_two])
        print("\nRelatório de classificação:")
        print(report)

    def get_confusion_matriz(self):
        self.conf_mat = confusion_matrix(self.y_teste, self.y_pred_test)
        print("Matriz de confusão:\n")
        print(self.conf_mat)

    def show_confusion_matriz(self):
        ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(self.y_teste, self.y_pred_test),
                               display_labels=self.pipeline.classes_).plot()
        plt.grid(False)
        plt.show()

    def make_learning_result(self):
        self.cross_validate_m(5)
        self.k_fold_m(1,5)
        self.show_k_fold_m_accuracies()
        self.show_classification_report()
        self.get_confusion_matriz()
        self.show_confusion_matriz()

