"""
classGrow classAsses 全部为自己编写。
"""

from classGrow import *
from classAsses import *
"""分类树主程序"""

# Growing
print('The tree is growing, wait a few seconds.')

T = classGrow('inputData/train.csv', 'tmp/reg/treeObj')
tree = T.tree

print('The tree is completely grown up!')

print('We are assessing the model, wait a few seconds.')

A = classAsses('inputData/test.csv', tree)
print('Accuracy is:', A.rate)

