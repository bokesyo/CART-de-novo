from classRef.matrix import *
from treePrint import *
from readData import *
data = local_cache('tmp/reg/144')
tree = data['tree']

data_dict = readCSV('inputData/train.csv')

node = tree.root.left.left

id_list = node.ID


mat_x = []
mat_y = []
for i in id_list:
    X = data_dict[i][0]
    mat_x.append(X)
    Y = [data_dict[i][1]]
    mat_y.append(Y)

print(mat_x)
print(mat_y)

