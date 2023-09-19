import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text
from sklearn.tree import _tree
import numpy as np
import pysubgroup as ps

class WrongPredicts:
    def __init__(self, df, test_data, classification_of_test_data, classification_of_test_data_in_array,
                 test_presence_values_list, predicts_by_algorithm):
        self.df = df
        self.error_data = test_data
        self.dataset_for_pyhard = None
        self.target = None
        self.searchspace = None
        self.task = None
        self.test_data = test_data
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
        self.tree_attributes = {'n_nodes': None, 'node_indicator': None, 'leaf_id': None}
    def define_number_of_items_in_dataset(self):
        pass
    #o find_positions era originalmente pra acahr posições com erros, atualmente ele insere na ultima coluna do dataframe os valores de erro

    def export_csv(self):
        self.error_data.to_csv('data.csv', index=False)
        print('CSV EXPORTADO')
        print(self.error_data.head(10))
    def find_positions_of_errors(self):
        for pos, prediction in enumerate(self.test_presence_values_list):
            self.error_data.iloc[pos, -1] = abs(self.y_teste_array[pos]-self.test_presence_values_list[pos])
            self.error_data.rename(columns={'presence': 'Class'}, inplace=True)

    def export_data_with_error_to_csv(self):
        self.dataset_for_pyhard = self.error_data
        # self.dataset_for_pyhard['Class'] = '"' + self.dataset_for_pyhard['Class'].astype(str) + '"'
        self.dataset_for_pyhard.to_csv('data.csv', index=False)
        # self.dataset_for_pyhard.reset_index(drop=True, inplace=True)
        # subset_df = self.dataset_for_pyhard.iloc[:81]
        # self.dataset_for_pyhard.to_csv('metadata.csv', index=False)

    def view_exported_data(self):
        print(self.dataset_for_pyhard.dtypes)

    def create_rule_fit_model(self):
        self.decision_tree = DecisionTreeRegressor(random_state=0, max_depth=3)
        self.decision_tree = self.decision_tree.fit(self.error_data.values[:, :-1], self.error_data.values[:, -1])

    def set_tree_attributes(self):
        self.tree_attributes['n_nodes'] = self.decision_tree.tree_.node_count
        self.tree_attributes['node_indicator'] = self.decision_tree.decision_path(self.error_data.values[:, :-1])
        self.tree_attributes['leaf_id'] = self.decision_tree.apply(self.error_data.values[:, :-1])

    def show_tree_attributes(self):
        for i in self.tree_attributes:
            print(i)
            print(self.tree_attributes[i])

    def extract_rules(self):
        self.df_column_names = self.error_data.drop('Class', axis=1).columns.tolist()
        self.rules = export_text(self.decision_tree, feature_names=self.df_column_names)

    def get_rules(self, tree, feature_names, class_names):
        #instanciando tree para chamar funções
        tree_ = tree.tree_
        #definindo nomes das features
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
            for i in tree_.feature
        ]

        paths = []
        path = []

        def recurse(node, path, paths):

            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                p1, p2 = list(path), list(path)
                p1 += [f"({name} <= {np.round(threshold, 3)})"]
                recurse(tree_.children_left[node], p1, paths)
                p2 += [f"({name} > {np.round(threshold, 3)})"]
                recurse(tree_.children_right[node], p2, paths)
            else:
                path += [(tree_.value[node], tree_.n_node_samples[node])]
                paths += [path]

        recurse(0, path, paths)

        # sort by samples count
        samples_count = [p[-1][1] for p in paths]
        ii = list(np.argsort(samples_count))
        paths = [paths[i] for i in reversed(ii)]

        rules = []
        for path in paths:
            rule = "if "

            for p in path[:-1]:
                if rule != "if ":
                    rule += " and "
                rule += str(p)
            rule += " then "
            if class_names is None:
                rule += "response: " + str(np.round(path[-1][0][0][0], 3))
            else:
                classes = path[-1][0][0]
                l = np.argmax(classes)
                rule += f"class: {class_names[l]} (proba: {np.round(100.0 * classes[l] / np.sum(classes), 2)}%)"
            rule += f" | based on {path[-1][1]:,} samples"
            rules += [rule]

        return rules

    def show_rules(self):
        print(self.rules)

    def show_df_head(self):
        print(self.same_rules_df.head())

    def define_pysubgroup_target(self):
        self.target = ps.BinaryTarget('Class', True)

    def define_pysubgroup_searchspace(self):
        self.searchspace = ps.create_selectors(self.test_data, ignore=['Class'])

    def define_pysubgroup_task(self):
        self.task = ps.SubgroupDiscoveryTask(
            self.test_data,
            self.target,
            self.searchspace,
            result_set_size=10,
            depth=2,
            qf=ps.WRAccQF())

    def get_pysubgroup_result(self):
        self.define_pysubgroup_target()
        self.define_pysubgroup_searchspace()
        self.define_pysubgroup_task()
        return ps.BeamSearch().execute(self.task)

    def make_comparisons(self):
        self.export_csv()
        self.find_positions_of_errors()
        print("ERROR DATA")
        print(self.error_data)
        self.create_rule_fit_model()
        self.set_tree_attributes()
        self.show_tree_attributes()
        self.extract_rules()
        # Caso não seja regressão:
        #rules = self.get_rules(self.decision_tree, self.df_column_names, self.error_data["Class"].unique().tolist())
        rules = self.get_rules(self.decision_tree, self.df_column_names, None)
        for r in rules:
            print(r)
        self.show_rules()
        result = self.get_pysubgroup_result()
        result = result.to_dataframe()
        pd.set_option('display.max_columns', None)

        #print(result.to_dataframe())
        print(result)
        #self.export_data_with_error_to_csv()
        #self.view_exported_data()
