from urllib.parse import parse_qs
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text

class WrongPredicts:
    def __init__(self, df, test_data, classification_of_test_data, classification_of_test_data_in_array,
                 test_presence_values_list, predicts_by_algorithm):
        self.df = df
        self.error_data = test_data
        self.classification_of_teste_data = classification_of_test_data
        self.predicts_by_algorithm = predicts_by_algorithm
        self.positions_of_errors = []
        self.number_of_lines_with_wrong_predicts = None
        self.same_rules = None
        self.same_rules_with_values = None
        self.are_items_the_same = False
        self.y_teste_array = classification_of_test_data_in_array
        self.test_presence_values_list = test_presence_values_list
        self.error_values_list = []
        #TODO implementar função para recuperar isso posteriormente
        self.number_of_items = 13
        self.same_rules_df = pd.DataFrame(columns=['two_rules', 'value_rule_one', 'value_rule_two'])
        self.rule_fit_model = None
        self.rules = None
        self.importances = None
        self.df_column_names = None
        self.final_rules = None
        self.decision_tree = None
    def define_number_of_items_in_dataset(self):
        pass
    #o find_positions era originalmente pra acahr posições com erros, atualmente ele insere na ultima coluna do dataframe os valores de erro
    def find_positions_of_errors(self):
        for pos, prediction in enumerate(self.test_presence_values_list):
            self.error_data.iloc[pos, -1] = abs(self.y_teste_array[pos]-self.test_presence_values_list[pos])
            self.error_data.rename(columns={'presence': 'Class'}, inplace=True)

    def create_rule_fit_model(self):
        self.decision_tree = DecisionTreeRegressor(random_state=0, max_depth=2)
        self.decision_tree = self.decision_tree.fit(self.error_data.values[:, :-1], self.error_data.values[:, -1])

    def extract_rules(self):
        self.df_column_names = self.error_data.drop('Class', axis=1).columns.tolist()
        self.rules = export_text(self.decision_tree, feature_names=self.df_column_names)

    def adjust_rules(self, rule):
        self.df_column_names = self.error_data.columns.tolist()

        for i, column_name in enumerate(self.df_column_names):
            rule = rule.replace(f'feature_{i}', column_name)
        return rule

    def show_rules(self):
        print(self.rules)

    def show_df_head(self):
        print(self.same_rules_df.head())

    def make_comparisons(self):
        self.find_positions_of_errors()
        print("ERROR DATA")
        print(self.error_data)
        self.create_rule_fit_model()
        self.extract_rules()
        self.show_rules()
