from regGrow import *
from regAsses import *

T = regGrow('inputData/partial_train.csv', 'tmp/reg/treeObj')
tree = T.tree

A = regAsses('inputData/test.csv', tree)

print('MSE:', A.mse, 'MAE:', A.mae, 'Accuracy(+-1):', A.rate)



