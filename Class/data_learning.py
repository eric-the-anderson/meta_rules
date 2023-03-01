#from Class.input_data import InputData
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
#try to make child class
#class DataLearning(InputData):
class DataLearning:

    def __init__(self, df, classificationColumnName):
        #super().__init__(df, classificationColumnName)
        self.df = df
        self.classificationColumnName = classificationColumnName
        self.pipeline = None
        self.predict = None
        self.x = None
        self.y = None
        self.X_treino = None
        self.X_teste = None
        self.y_treino = None
        self.y_teste = None
        self.y_treino_array = None

    def define_x(self):
        self.x = self.df.drop(self.classificationColumnName, axis=1)

    def define_y(self):
        self.y = self.df[self.classificationColumnName]

    def partition_data(self):
        self.X_treino, self.X_teste, self.y_treino, self.y_teste = train_test_split(self.x, self.y, test_size=0.3,
                                                                                    shuffle=False)

    def create_pipeline(self):
        self.pipeline = Pipeline(steps=[
    ("normalizacao", MinMaxScaler()),
    ("Decisiontree", DecisionTreeClassifier(max_depth=None, random_state=0))
])

    def train_data(self):
        self.pipeline.fit(self.X_treino, self.y_treino)

    def get_classification_of_data(self):
        self.y_treino_array = self.y_treino.to_numpy()

    def make_predict(self):
        self.predict = self.pipeline.predict(self.X_treino)

    def make_data_learning(self):
        self.define_x()
        self.define_y()
        self.partition_data()
        self.create_pipeline()
        self.train_data()
        self.get_classification_of_data()
        self.make_predict()