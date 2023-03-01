from Class.input_data import InputData
from Class.data_learning import DataLearning


path = 'C:\\Users\\erica\\OneDrive\\Documentos\\projects\\meta_rules\\resources\\dataset\\statlog.csv'
input_data = InputData(path)
input_data.make_full_exploratory_analysis()

data_learning = DataLearning(input_data.df, input_data.classificationColumnName)
data_learning.make_data_learning()