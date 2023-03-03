from urllib.parse import parse_qs
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
        self.same_rules_dict = {}
        self.same_rules_with_values = {}
    def define_number_of_items_in_dataset(self):
        pass
    def find_positions_of_errors(self):
        for pos, prediction in enumerate(self.y_treino):
            if self.y_treino_array[pos] != self.predicts_by_algorithm[pos]:
                self.positions_of_errors.append(pos)
                print("position" + str(pos) + " have a dataset predict value:" + str(
                    prediction) + " but the algorithm predicted:" + str(self.predicts_by_algorithm[pos]))

    def compare_two_items(self, item_one, item_two):
        if item_one == item_two:
            return True

    def compare_two_lines(self, line_one, line_two):
        self.compare_all_wrong_predict_items(self.number_of_items, line_one,
                                        line_two)

    def compare_all_wrong_predict_lines(self, line_list):
        for i in self.positions_of_errors:
            while i < self.positions_of_errors[-1]:
                for j in self.positions_of_errors:
                    while j < self.positions_of_errors[-1]:
                        self.compare_two_lines(self.number_of_items, i, j + 1)

    def compare_all_wrong_predict_items(self, line_one, line_two):
        dict_key = ''
        for i in range(self.number_of_items):
            are_items_the_same = False
            are_items_the_same = self.compare_two_items(self.df.iloc[line_one, i],
                                                   self.df.iloc[line_two, i])
            if are_items_the_same:
                # dict_key =
                print("put in the dict")

    def are_pair_of_rules_found(self, rule_one, rule_two):
        same_rules = self.same_rules + rule_one + ' ' + rule_two
        try:
            self.same_rules_dict[same_rules] = self.same_rules_dict[same_rules] + 1
        except:
            self.same_rules_dict[same_rules] = 1

