from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

class DataLearning:

    def __init__(self, df, classificationColumnName):
        #super().__init__(df, classificationColumnName)
        self.df = df
        self.classificationColumnName = classificationColumnName
        self.pipeline = None
        self.pred= None
        self.pred_test = None
        self.train_probabilities = None
        self.test_probabilities = None
        self.x = None
        self.y = None
        self.X_treino = None
        self.X_teste = None
        self.y_treino = None
        self.y_teste = None
        self.y_treino_array = None
        self.y_test_array = None
        #apenas para teste abaixo
        self.class_one = '1'
        self.class_two = '2'
        self.train_absence_values_list = []
        self.train_presence_values_list = []
        self.test_absence_values_list = []
        self.test_presence_values_list = []

    def define_x(self):
        self.x = self.df.drop(self.classificationColumnName, axis=1)

    def define_y(self):
        self.y = self.df[self.classificationColumnName]

    def partition_data(self):
        #self.X_treino, self.X_teste, self.y_treino, self.y_teste = train_test_split(self.x, self.y, test_size=0.3,
                                                                                    #shuffle=True, random_state=32)
        self.X_treino, self.X_teste, self.y_treino, self.y_teste = train_test_split(self.x, self.y, test_size=0.3,
                                                                                    shuffle=False)
        print('CONTAAGEM DE VALORES')
        print(self.y_treino.value_counts())

    def create_pipeline(self):
        self.pipeline = Pipeline(steps=[
    ("normalizacao", MinMaxScaler()),
    ("classifier", RandomForestClassifier(n_estimators=5, random_state=0))
    #("Decisiontree", DecisionTreeClassifier(max_depth=5, random_state=32))
])

    def train_data(self):
        self.pipeline.fit(self.X_treino, self.y_treino)

    def get_classification_of_data(self):
        self.y_treino_array = self.y_treino.to_numpy()

    def get_classification_of_test_data(self):
        self.y_test_array = self.y_teste.to_numpy()

    #perde muita informação, remover
    def make_predict(self):
        self.pred = self.pipeline.predict(self.X_treino)
        print('y treino')
        print(self.y_treino_array)
        print('y pred')
        print(self.pred)
        report = classification_report(self.y_treino, self.pred, target_names=[self.class_one, self.class_two])
        print("\nRelatório de classificação:")
        print(report)
    def make_predict_test(self):
        self.pred_test = self.pipeline.predict(self.X_teste)

    def make_test_probabilities(self):
        self.test_probabilities = self.pipeline.predict_proba(self.X_teste)
    def make_train_probalities(self):
        self.train_probabilities = self.pipeline.predict_proba(self.X_treino)

    def make_probabilities_train_of_presence_list(self):
        self.train_absence_values_list = []
        self.train_presence_values_list = []
        for i in range (len(self.train_probabilities)):
            # self.train_absence_values_list.append(self.train_probabilities[i][0])
            self.train_presence_values_list.append(self.train_probabilities[i][1])

    def make_probabilities_test_of_presence_list(self):
        self.test_absence_values_list = []
        self.test_presence_values_list = []
        for i in range (len(self.test_probabilities)):
            # self.test_absence_values_list.append(self.test_probabilities[i][0])
            self.test_presence_values_list.append(self.test_probabilities[i][1])

    def add_presence_rows_in_df(self):
        # self.X_treino['absence'] = self.train_absence_values_list
        self.X_treino['presence'] = self.train_presence_values_list
        # self.X_teste['absence'] = self.test_absence_values_list
        self.X_teste['presence'] = self.test_presence_values_list

    def make_data_learning(self):
        self.define_x()
        self.define_y()
        self.partition_data()
        self.create_pipeline()
        self.train_data()
        self.get_classification_of_data()
        self.get_classification_of_test_data()
        self.make_predict()
        self.make_predict_test()
        self.make_test_probabilities()
        self.make_train_probalities()
        self.make_probabilities_train_of_presence_list()
        self.make_probabilities_test_of_presence_list()
        self.add_presence_rows_in_df()
        print(self.train_probabilities)