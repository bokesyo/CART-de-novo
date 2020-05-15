from regGrow import *
from regAsses import *
from regPrune import *
from readData import *

data_dict = readCSV('inputData/partial_train.csv')

print('The tree is growing, please wait a few seconds. (About 5 seconds on MacBook Pro)')
# Growing
T = regGrow('inputData/partial_train.csv', 'tmp/reg/treeObj')
tree = T.tree
print('Grown up!')

print('Start pruning')
# Pruning
stop = False
n = 1

while tree.size > 1:
    this = regPrune(tree, data_dict)
    tree = this.tree
    print('This is the', str(n), 'th pruning.')
    data = local_cache('tmp/reg/forest/' + str(n))
    data['tree'] = tree
    n = n + 1

print('Pruning is finished.')


print('Cross validation starts.')


# Filtering
m = 1
tup_list = []
for i in range(1, n - 1):
    data = local_cache('tmp/reg/forest/' + str(m))
    tree = data['tree']
    A = regAsses('inputData/remain_train.csv', tree)
    print('This is the ', m, 'th candidate tree, MSE is', A.mse, ', MAE is', A.mae, ', Accuracy is ', A.rate)
    tup = (m, A.mse)
    tup_list.append(tup)
    m = m + 1


optimal = None
for tup in tup_list:
    if not optimal:
        optimal = tup
    else:
        if tup[1] < optimal[1]:
            optimal = tup


print(optimal[0], 'th candidate is the optimized tree with a MSE of ', optimal[1])

print('Cross validation ends.')


# Testing
print('Testing begins.')

data = local_cache('tmp/reg/forest/' + str(optimal[0]))
tree = data['tree']
A = regAsses('inputData/test.csv', tree)
print('MSE is', A.mse, ', MAE is', A.mae, ', Accuracy is ', A.rate)

print('Testing finished.')

