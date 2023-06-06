import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


class InputData:

    def __init__(self, path):
        self.datasetPath = path
        self.df = None
        self.areDatasetOk = False
        self.classificationColumnName = ''

    def create_pd_dataframe(self):
        self.df = pd.read_csv(self.datasetPath)

    def get_classification_column_name(self):
        self.classificationColumnName = self.df.columns[-1]

    def change_class_target_for_zero_and_one(self):
        self.df[self.classificationColumnName].replace({'1': '0', '2': '1'})

    # provavelmente não usarei o método abaixo
    def check_dataset(self, dataset):
        pass

    def head_of_dataset(self):
        print("Dataset Head: ")
        print(self.df.head())

    def count_values(self):
        print("Count Values of Dataset")
        print(self.df[self.classificationColumnName].value_counts())

    def plot_pie(self):
        plt.pie = self.df[self.classificationColumnName].value_counts().plot.pie(autopct='%.2f')
        plt.show()

    def dataset_shape(self):
        print("\nDataset Shape: ")
        print(f'Linhas: {self.df.shape[0]}')
        print(f'Colunas: {self.df.shape[1]}')

    def dataset_data_types(self):
        print("\nDataset Data Types: ")
        print(self.df.dtypes)

    def check_null_data(self):
        print("\nCheck if exists null data in dataset: ")
        print(self.df.isna().sum())

    def make_full_exploratory_analysis(self):
        self.create_pd_dataframe()
        self.head_of_dataset()
        self.get_classification_column_name()
        self.change_class_target_for_zero_and_one()
        self.count_values()
        self.dataset_shape()
        self.dataset_data_types()
        self.check_null_data()
        self.plot_pie()

# path = "/content/drive/MyDrive/Mestrado/Reunioes_com_orientador/Orientacao_Individual/artigo_de_metaregras/statlog.csv"
# df = pd.read_csv(path)
# df.head()
