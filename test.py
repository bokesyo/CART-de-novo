from readData import *
from tmp.reg.exe import *

test_data = readCSV('inputData/test.csv')

n = 0
m = 0
for i in test_data:
    mat = test_data[i][0]
    obs = test_data[i][1]
    pre = classifier(mat)
    moment = (pre - obs) ** 2
    m += moment
    print(obs, pre, moment)
    n += 1

print('@@@', m / n)
