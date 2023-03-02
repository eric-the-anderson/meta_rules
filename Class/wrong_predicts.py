
class WrongPredicts:
    def __init__(self, classification_of_data, classification_of_data_in_array, predicts_by_algorithm):
        self.classification_of_data = classification_of_data
        self.predicts_by_algorithm = predicts_by_algorithm
        self.positions_of_errors = []
        self.number_of_lines_with_wrong_predicts = None
        self.same_rules = None
        self.same_rules_with_values = None
        self.are_items_the_same = False
        self.y_treino = classification_of_data
        self.y_treino_array = classification_of_data_in_array

    def find_positions_of_errors(self):
        for pos, prediction in enumerate(self.y_treino):
            if self.y_treino_array[pos] != self.predicts_by_algorithm[pos]:
                self.positions_of_errors.append(pos)
                print("position" + str(pos) + " have a dataset predict value:" + str(
                    prediction) + " but the algorithm predicted:" + str(self.predicts_by_algorithm[pos]))

    def compare_two_items(self, item_one, item_two):
        pass

    def compare_two_lines(self, line_one, line_two):
        pass

    def compare_all_wrong_predict_lines(self, line_list):
        pass

    def compare_all_wrong_predict_items(self, predict_items):
        pass

    def are_pair_of_rules_found(self):
        pass

