from regGrow import *
from regAsses import *
from regPrune import *
from readData import *

data_dict = readCSV('inputData/partial_train.csv')

# Growing
T = regGrow('inputData/partial_train.csv', 'tmp/reg/treeObj')
tree = T.tree


# Pruning
stop = False
n = 1

while tree.size > 1:
    this = regPrune(tree, data_dict)
    tree = this.tree
    data = local_cache('tmp/reg/forest/' + str(n))
    data['tree'] = tree
    n = n + 1


# Filtering
m = 1
for i in range(1, n - 1):
    data = local_cache('tmp/reg/forest/' + str(m))
    tree = data['tree']
    A = regAsses('inputData/remain_train.csv', tree)
    print(m, ',', A.mse, ',', A.mae, ',', A.rate)
    m = m + 1
