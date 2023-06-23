from urllib.parse import parse_qs
import pandas as pd
import Orange

class WrongPredicts:
    def __init__(self, df, test_data, classification_of_test_data, classification_of_test_data_in_array,
                 test_presence_values_list, predicts_by_algorithm):
        self.df = df
        #o error_data deve ser os dados de treino
        self.error_data = test_data
        # self.classification_of_data = classification_of_data
        self.classification_of_teste_data = classification_of_test_data
        self.predicts_by_algorithm = predicts_by_algorithm
        self.positions_of_errors = []
        self.number_of_lines_with_wrong_predicts = None
        self.same_rules = None
        self.same_rules_with_values = None
        self.are_items_the_same = False
        # self.y_treino = classification_of_
        # self.y_treino_array = classification_of_data_in_array
        self.y_teste_array = classification_of_test_data_in_array
        # self.train_presence_values_list = train_presence_values_list
        # self.train_absence_values_list = train_absence_values_list
        self.test_presence_values_list = test_presence_values_list
        # self.test_absence_values_list = test_absence_values_list
        self.error_values_list = []
        #implementar função para recuperar isso posteriormente
        self.number_of_items = 13
        self.same_rules_df = pd.DataFrame(columns=['two_rules', 'value_rule_one', 'value_rule_two'])
        #self.same_rules_with_values = {}
        self.lim_e = 0.1
        self.lim_c = 0.05
        self.orange_table = None
        self.orange_domain = None
        self.orange_data = None
        self.orange_model = None

    def define_number_of_items_in_dataset(self):
        pass
    #o find_positions era originalmente pra acahr posições com erros, atualmente ele insere na ultima coluna do dataframe os valores de erro
    def find_positions_of_errors(self):
        for pos, prediction in enumerate(self.test_presence_values_list):
            self.error_data.iloc[pos, -1] = abs(self.y_teste_array[pos]-self.test_presence_values_list[pos])
            self.error_data.rename(columns={'presence': 'c#Class'}, inplace=True)

    def create_orange_domain(self):
        domain_attributes = [Orange.data.ContinuousVariable(col) for col in self.error_data.columns[:-1]]
        class_var = Orange.data.ContinuousVariable(self.error_data.columns[-1])
        self.orange_domain = Orange.data.Domain(domain_attributes, class_var)

    def create_orange_table(self):
        # self.orange_table = Orange.data.Table(self.orange_domain)
        self.orange_table = Orange.data.Table.from_numpy(domain=self.orange_domain, X=self.error_data.values[:, :-1],
                                                         Y=self.error_data.values[:, -1])


    def convert_pandas_to_orange(self, df):
        self.create_orange_domain()
        self.create_orange_table()

    def extract_rules(self):
        print(self.orange_table.Y)
        learner = Orange.classification.rules.CN2Learner()
        self.orange_model = learner(self.orange_table)

    def show_rules(self):
        new_data = Orange.data.Table.from_domain(self.orange_model.domain, self.error_data.values)
        predictions = self.orange_model(new_data)

        for prediction in predictions:
            print(prediction)

    # def compare_two_items(self, item_one, item_two):
    #     if item_one == item_two:
    #         return True
    #
    # def compare_two_lines(self, line_one, line_two):
    #     self.compare_all_wrong_predict_items(line_one, line_two)
    #
    # def compare_all_wrong_predict_lines(self):
    #     first_step = 0
    #     are_first_step = False
    #
    #     for i in range(len(self.positions_of_errors)):
    #         first_step = first_step + 1
    #         are_first_step = True
    #         if self.positions_of_errors[i] < self.positions_of_errors[-1]:
    #             for j in range(len(self.positions_of_errors)):
    #                 if self.positions_of_errors[j] < self.positions_of_errors[-1]:
    #                     if are_first_step:
    #                         self.compare_two_lines(self.positions_of_errors[i], self.positions_of_errors[j+first_step])
    #                     else:
    #                         if j+1 > first_step:
    #                             self.compare_two_lines(self.positions_of_errors[i],
    #                                                    self.positions_of_errors[j + 1])
    #                     are_first_step = False
    # def compare_all_wrong_predict_items(self, line_one, line_two):
    #     rule_list = []
    #     rule_values = []
    #     for i in range(self.number_of_items):
    #         are_items_the_same = False
    #         are_items_the_same = self.compare_two_items(self.df.iloc[line_one, i], self.df.iloc[line_two, i])
    #         if are_items_the_same:
    #             # rule_one_name = ''#aqui vai ser inserida uma string com o nome da coluna em questão
    #             # value_rule_one = self.df.iloc[line_one, i]
    #             # self.find_rule_two(line_one, i)
    #             rule_list.append(self.df.columns[i])
    #             rule_values.append(self.df.iloc[line_one, i])
    #
    #     self.save_infos_in_same_rules_df(rule_list, rule_values)
    #
    # def find_rule_two(self, line_one, column_pos):
    #     pass
    #
    # def are_pair_of_rules_found(self, rule_one, rule_two):
    #     same_rules = self.same_rules + rule_one + ' ' + rule_two
    #     try:
    #         self.same_rules_dict[same_rules] = self.same_rules_dict[same_rules] + 1
    #     except:
    #         self.same_rules_dict[same_rules] = 1
    #
    # def save_infos_in_same_rules_df(self, rule_list, rule_values):
    #     items_of_row = []
    #     two_rules_name = ''
    #     value_of_rule_one = None
    #     value_of_rule_two = None
    #     first_step = 0
    #     are_first_step = False
    #
    #     for i in range(len(rule_list)):
    #         if rule_list[i] < rule_list[-1]:
    #             for j in range(len(rule_list)):
    #                 if rule_list[j] < rule_list[-1]:
    #                     if are_first_step:
    #                         # print('pos_two')
    #                         # print(pos_two)
    #                         # print('rule list len')
    #                         # print(len(rule_list))
    #                         items_of_row = []
    #                         two_rules_name = ''
    #                         value_of_rule_one = None
    #                         value_of_rule_two = None
    #                         #conferir se essas checagens acima realmente estão corretas
    #
    #                         # print('I')
    #                         # print(i)
    #                         # print('rule list')
    #                         # print(rule_list[pos_two+1])
    #                         two_rules_name = str(rule_list[i])+'-'+str(rule_list[j+first_step])
    #                         value_of_rule_one = rule_values[i]
    #                         value_of_rule_two = rule_values[j+first_step]
    #                         items_of_row.append(two_rules_name)
    #                         items_of_row.append(value_of_rule_one)
    #                         items_of_row.append(value_of_rule_two)
    #                         self.same_rules_df.loc[len(self.same_rules_df)] = items_of_row
    #                         print(self.same_rules_df.head())
    #                     else:
    #                         if j+1 > first_step:
    #                             items_of_row = []
    #                             two_rules_name = ''
    #                             value_of_rule_one = None
    #                             value_of_rule_two = None
    #                             # conferir se essas checagens acima realmente estão corretas
    #
    #                             # print('I')
    #                             # print(i)
    #                             # print('rule list')
    #                             # print(rule_list[pos_two+1])
    #                             two_rules_name = str(rule_list[i]) + '-' + str(rule_list[j + 1])
    #                             print(two_rules_name)
    #                             value_of_rule_one = rule_values[i]
    #                             value_of_rule_two = rule_values[j + 1]
    #                             items_of_row.append(two_rules_name)
    #                             items_of_row.append(value_of_rule_one)
    #                             items_of_row.append(value_of_rule_two)
    #                             self.same_rules_df.loc[len(self.same_rules_df)] = items_of_row
    #                             #print(self.same_rules_df.head())
    #                     are_first_step = False

    def show_df_head(self):
        print(self.same_rules_df.head())

    def make_comparisons(self):
        self.find_positions_of_errors()
        print("ERROR DATA")
        print(self.error_data)
        self.convert_pandas_to_orange(self.error_data)
        self.extract_rules()
        self.show_rules()
        # self.compare_all_wrong_predict_lines()
        # self.show_df_head()