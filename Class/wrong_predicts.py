from urllib.parse import parse_qs
import pandas as pd

class WrongPredicts:
    def __init__(self, df, classification_of_data, classification_of_data_in_array, predicts_by_algorithm):
        self.df = df
        self.classification_of_data = classification_of_data
        self.predicts_by_algorithm = predicts_by_algorithm
        self.positions_of_errors = []
        self.number_of_lines_with_wrong_predicts = None
        self.same_rules = None
        self.same_rules_with_values = None
        self.are_items_the_same = False
        self.y_treino = classification_of_data
        self.y_treino_array = classification_of_data_in_array
        #implementar função para recuperar isso posteriormente
        self.number_of_items = 13
        self.same_rules_df = pd.DataFrame(columns=['two_rules', 'value_rule_one', 'value_rule_two'])
        #self.same_rules_with_values = {}

    def define_number_of_items_in_dataset(self):
        pass

    def find_positions_of_errors(self):
        # testes
        # print('y treino')
        # print(self.y_treino)
        # print('y treino_array')
        # print(self.y_treino_array)
        # print('predicts by algorithm')
        # print(self.predicts_by_algorithm)
        # testes
        for pos, prediction in enumerate(self.y_treino):
            if self.y_treino_array[pos] != self.predicts_by_algorithm[pos]:
                self.positions_of_errors.append(pos)
                print("position" + str(pos) + " have a dataset predict value:" + str(
                    prediction) + " but the algorithm predicted:" + str(self.predicts_by_algorithm[pos]))

    def compare_two_items(self, item_one, item_two):
        if item_one == item_two:
            return True

    def compare_two_lines(self, line_one, line_two):
        self.compare_all_wrong_predict_items(line_one, line_two)

    def compare_all_wrong_predict_lines(self):
        for i in self.positions_of_errors:
            while i < self.positions_of_errors[-1]:
                for pos, j in enumerate(self.positions_of_errors):
                    while j < self.positions_of_errors[-1]:
                        self.compare_two_lines(i, self.positions_of_errors[pos+1])

    def compare_all_wrong_predict_items(self, line_one, line_two):
        rule_list = []
        rule_values = []
        for i in range(self.number_of_items):
            are_items_the_same = False
            are_items_the_same = self.compare_two_items(self.df.iloc[line_one, i], self.df.iloc[line_two, i])
            if are_items_the_same:
                # rule_one_name = ''#aqui vai ser inserida uma string com o nome da coluna em questão
                # value_rule_one = self.df.iloc[line_one, i]
                # self.find_rule_two(line_one, i)
                rule_list.append(self.df.columns[i])
                rule_values.append(self.df.iloc[line_one, i])

        self.save_infos_in_same_rules_df(rule_list, rule_values)

    def find_rule_two(self, line_one, column_pos):
        pass

    def are_pair_of_rules_found(self, rule_one, rule_two):
        same_rules = self.same_rules + rule_one + ' ' + rule_two
        try:
            self.same_rules_dict[same_rules] = self.same_rules_dict[same_rules] + 1
        except:
            self.same_rules_dict[same_rules] = 1

    def save_infos_in_same_rules_df(self, rule_list, rule_values):
        items_of_row = []
        two_rules_name = ''
        value_of_rule_one = None
        value_of_rule_two = None
        for pos, i in enumerate(rule_list):
            while pos < len(rule_list):
                for pos_two, j in enumerate(rule_list):
                    if pos_two >= pos:
                        while pos_two < len(rule_list):
                            print('pos_two')
                            print(pos_two)
                            print('rule list len')
                            print(len(rule_list))
                            items_of_row = []
                            two_rules_name = ''
                            value_of_rule_one = None
                            value_of_rule_two = None
                            #conferir se essas checagens acima realmente estão corretas

                            # print('I')
                            # print(i)
                            # print('rule list')
                            # print(rule_list[pos_two+1])
                            two_rules_name = str(i)+'-'+str(rule_list[pos_two+1])
                            value_of_rule_one = rule_values[pos]
                            value_of_rule_two = rule_values[pos_two+1]
                            items_of_row.append(two_rules_name)
                            items_of_row.append(value_of_rule_one)
                            items_of_row.append(value_of_rule_two)
                            self.same_rules_df.loc[len(self.same_rules_df)] = items_of_row
                            print(self.same_rules_df.head())

    def show_df_head(self):
        print(self.same_rules_df.head())

    def make_comparisons(self):
        self.find_positions_of_errors()
        self.compare_all_wrong_predict_lines()
        self.show_df_head()