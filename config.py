assessment_dataset = 'inputData/test.csv'

primary_tree_object = 'dataStorge/primaryTreeObject'

execute_classifier = "output/generalExecute.py"

train_dataset = 'inputData/train.csv'

pointer_name = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

tree_graph_output = "output/treePrint.eps"

number_of_col = 12



"""

On input format:

1. The first row is not included, because it is our pointer row

2. The following rows are included

3. The last column is not included, because it is our target function

4. The latter columns are included

"""