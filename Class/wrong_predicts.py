from urllib.parse import parse_qs
import pandas as pd

class WrongPredicts:
    def __init__(self, df, classification_of_data, classification_of_data_in_array, train_presence_values_list, train_absence_values_list,
                 predicts_by_algorithm):
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
        self.train_presence_values_list = train_presence_values_list
        self.train_absence_values_list = train_absence_values_list
        self.error_values_list = []
        #implementar função para recuperar isso posteriormente
        self.number_of_items = 13
        self.same_rules_df = pd.DataFrame(columns=['two_rules', 'value_rule_one', 'value_rule_two'])
        #self.same_rules_with_values = {}


    def define_number_of_items_in_dataset(self):
        pass

    def find_positions_of_errors(self):
        for pos, prediction in enumerate(self.train_absence_values_list):
            if self.classification_of_data[pos] == '1':
                if self.train_presence_values_list[pos] < self.train_absence_values_list[pos]:
                    self.positions_of_errors.append(pos)
                    print("position" + str(pos) + " have a classification '1' but the biggest proba of prediction is '"
                                                  "2' absence " + str(self.train_absence_values_list[pos]))
                    self.error_values_list.append(1-self.train_absence_values_list)
                else:
                    self.error_values_list.append(1-self.train_presence_values_list)

            if self.classification_of_data[pos] == '2':
                if self.train_absence_values_list[pos] < self.train_presence_values_list[pos]:
                    self.positions_of_errors.append(pos)
                    print("position" + str(pos) + " have a classification '2' but the biggest proba of prediction is '"
                                                  "1' presence " + str(self.train_presence_values_list[pos]))
                    self.error_values_list.append(1-self.train_presence_values_list)
                else:
                    self.error_values_list.append(1-self.train_absence_values_list)
                    
    def compare_two_items(self, item_one, item_two):
        if item_one == item_two:
            return True

    def compare_two_lines(self, line_one, line_two):
        self.compare_all_wrong_predict_items(line_one, line_two)

    def compare_all_wrong_predict_lines(self):
        first_step = 0
        are_first_step = False

        for i in range(len(self.positions_of_errors)):
            first_step = first_step + 1
            are_first_step = True
            if self.positions_of_errors[i] < self.positions_of_errors[-1]:
                for j in range(len(self.positions_of_errors)):
                    if self.positions_of_errors[j] < self.positions_of_errors[-1]:
                        if are_first_step:
                            self.compare_two_lines(self.positions_of_errors[i], self.positions_of_errors[j+first_step])
                        else:
                            if j+1 > first_step:
                                self.compare_two_lines(self.positions_of_errors[i],
                                                       self.positions_of_errors[j + 1])
                        are_first_step = False
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
        first_step = 0
        are_first_step = False

        for i in range(len(rule_list)):
            if rule_list[i] < rule_list[-1]:
                for j in range(len(rule_list)):
                    if rule_list[j] < rule_list[-1]:
                        if are_first_step:
                            # print('pos_two')
                            # print(pos_two)
                            # print('rule list len')
                            # print(len(rule_list))
                            items_of_row = []
                            two_rules_name = ''
                            value_of_rule_one = None
                            value_of_rule_two = None
                            #conferir se essas checagens acima realmente estão corretas

                            # print('I')
                            # print(i)
                            # print('rule list')
                            # print(rule_list[pos_two+1])
                            two_rules_name = str(rule_list[i])+'-'+str(rule_list[j+first_step])
                            value_of_rule_one = rule_values[i]
                            value_of_rule_two = rule_values[j+first_step]
                            items_of_row.append(two_rules_name)
                            items_of_row.append(value_of_rule_one)
                            items_of_row.append(value_of_rule_two)
                            self.same_rules_df.loc[len(self.same_rules_df)] = items_of_row
                            print(self.same_rules_df.head())
                        else:
                            if j+1 > first_step:
                                items_of_row = []
                                two_rules_name = ''
                                value_of_rule_one = None
                                value_of_rule_two = None
                                # conferir se essas checagens acima realmente estão corretas

                                # print('I')
                                # print(i)
                                # print('rule list')
                                # print(rule_list[pos_two+1])
                                two_rules_name = str(rule_list[i]) + '-' + str(rule_list[j + 1])
                                print(two_rules_name)
                                value_of_rule_one = rule_values[i]
                                value_of_rule_two = rule_values[j + 1]
                                items_of_row.append(two_rules_name)
                                items_of_row.append(value_of_rule_one)
                                items_of_row.append(value_of_rule_two)
                                self.same_rules_df.loc[len(self.same_rules_df)] = items_of_row
                                #print(self.same_rules_df.head())
                        are_first_step = False

    def show_df_head(self):
        print(self.same_rules_df.head())

    def make_comparisons(self):
        self.find_positions_of_errors()
        self.compare_all_wrong_predict_lines()
        self.show_df_head()