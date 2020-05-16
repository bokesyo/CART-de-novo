from linearReg import *
from readData import *
from classRef.localCache import *
from compile import *
from classRef.matrix import *


class Regress:
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.id_list = list(range(0, len(data_dict)))
        self.beta = None
        self.regress()

    def regress(self):
        mat_x = []
        mat_y = []
        for i in self.id_list:
            X = [1] + self.data_dict[i][0]
            mat_x.append(X)
            Y = [self.data_dict[i][1]]
            mat_y.append(Y)
        self.beta = multiply(reverse(multiply(transfer(mat_x), mat_x)), multiply(transfer(mat_x), mat_y))


data_dict = readCSV('inputData/train copy.csv')

test_dict = readCSV('inputData/test copy.csv')

R = Regress(data_dict)

beta = R.beta

n = 0
constant = beta[0][0]
del beta[0]


moment = 0
for i in test_dict:
    var = constant
    obs = test_dict[i][1]
    print(obs)
    mat = test_dict[i][0]
    print(mat)
    for j in range(0, len(mat)):
        product = beta[j][0] * mat[j]
        var += product
    print(var)
    moment += (var - obs) ** 2

mse = moment / len(test_dict)

print(mse)

