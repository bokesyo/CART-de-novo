from regGrow import *
from regAsses import *
from regPrune import *
from readData import *

data = local_cache('tmp/reg/144')
tree = data['tree']
A = regAsses('inputData/test.csv', tree)
print('th tree is the optimal tree, MSE is', A.mse, 'R2 is', A.R2, 'Cor is', A.cor)


print('Testing finished.')

