from classGrow import *
from classAssessment import *

T = treeGrow('inputData/train.csv', 'tmp/reg/classObj')
tree = T.tree

A = classAssess('dataProcess/wine.csv', tree)
rate = A.rate

print(rate)



