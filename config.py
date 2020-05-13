assessment_dataset = 'inputData/test.csv'

train_dataset = 'inputData/partial_train.csv'

pointer_name = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

number_of_col = 12

reg_graph_output = "tmp/regPrint.eps"
class_graph_output = "tmp/classPrint.eps"


class_tree_object = 'tmp/classTreeObject'
reg_tree_object = 'tmp/regTreeObject'


class_execute_classifier = "tmp/classExecute.py"
reg_execute_classifier = "tmp/regExecute.py"


"""

On input format:

1. The first row is not included, because it is our pointer row

2. The following rows are included

3. The last column is not included, because it is our target function

4. The latter columns are included

"""