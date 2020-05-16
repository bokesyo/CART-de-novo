from readData import *
from tmp.reg.exe import *


test_data = readCSV('inputData/test.csv')


n = 0
m = 0
for i in test_data:
    mat = test_data[i][0]
    obs = test_data[i][1]
    pre = classifier(mat)
    # if (pre>8):
    #     pre = 8
    # elif (pre<3):
    #     pre = 3
    moment = (pre - obs) ** 2
    m += moment
    print(obs, ',', pre, ',', moment)
    n += 1

print('@@@', m / n)

"""
[[44.53140643192455], 
[0.032033538427370445], 
[-1.1590798312424653], 

[-0.23767511163526933], 
[0.04482276679829056], 
[-1.2349477215879006], 

[-0.003240450153720875], 
[-0.0028084452867707943], 
[-41.11244057324075], 

[-0.18648298536959373], 
[0.8539692392145923], 
[0.2620655505742491]]
"""

