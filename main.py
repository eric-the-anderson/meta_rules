from Class.input_data import InputData
from Class.data_learning import DataLearning
from Class.learning_result import LearningResult
from Class.wrong_predicts import WrongPredicts


path = 'C:\\Users\\erica\\OneDrive\\Documentos\\projects\\meta_rules\\resources\\dataset\\statlog.csv'
# path = 'C:\\Users\\erica\\OneDrive\\Documentos\\projects\\meta_rules\\resources\\dataset\\diabetes.csv'
# path = 'C:\\Users\\erica\\OneDrive\\Documentos\\projects\\meta_rules\\resources\\dataset\\water_potability.csv'
# path = 'C:\\Users\\erica\\OneDrive\\Documentos\\projects\\meta_rules\\resources\\dataset\\predictive_maintenance.csv'
# path = 'C:\\Users\\erica\\OneDrive\\Documentos\\projects\\meta_rules\\resources\\dataset\\fake_job_postings.csv'

input_data = InputData(path)
input_data.make_full_exploratory_analysis()

data_learning = DataLearning(input_data.df, input_data.classificationColumnName)
data_learning.make_data_learning()

learning_result = LearningResult(data_learning.pipeline, data_learning.x, data_learning.y,
                                 data_learning.X_treino, data_learning.y_teste,
                                 data_learning.pred, data_learning.pred_test)
learning_result.make_learning_result()

wrong_predicts = WrongPredicts(input_data.df, data_learning.X_teste, data_learning.y_teste, data_learning.y_test_array,
                               data_learning.test_presence_values_list, data_learning.pred_test)
wrong_predicts.make_comparisons()