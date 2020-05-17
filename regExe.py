"""
直接上 「多元线性回归」，查看 MSE

M5 ： 自己编写的 「多元线性回归」类
"""

from M5 import *
from compile import *


class Regress:
    """
    最基本的回归
    """
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


def corr(list1, list2):
    """

    :param list1: 自变量
    :param list2: 因变量
    :return: 相关系数
    """
    sum_x_y = 0
    sum_x_x = 0
    sum_x = 0
    sum_y = 0
    sum_y_y = 0
    n = len(list1)
    for j in range(0, n):
        x_y = list1[j] * list2[j]
        sum_x_y += x_y
        x_x = list1[j] ** 2
        sum_x_x += x_x
        y_y = list2[j] ** 2
        sum_y_y += y_y
        x = list1[j]
        sum_x += x
        y = list2[j]
        sum_y += y
    b = ((n * sum_x_y) - sum_x * sum_y) / (n * sum_x_x - sum_x ** 2)
    a = (sum_y - b * sum_x) / n
    r = (n * sum_x_y - sum_x * sum_y) / ((n * sum_x_x - sum_x ** 2) * (n * sum_y_y - sum_y ** 2)) ** 0.5
    return r


data_dict = readCSV('inputData/train.csv')

test_dict = readCSV('inputData/test.csv')

R = Regress(data_dict)
print(R.beta)
beta = R.beta

n = 0
constant = beta[0][0]
del beta[0]


# 验证
mat_x = []
mat_y = []
moment = 0
for i in test_dict:
    var = constant
    obs = test_dict[i][1]
    mat_x.append(obs)
    # print(obs)
    mat = test_dict[i][0]
    # print(mat)
    for j in range(0, len(mat)):
        product = beta[j][0] * mat[j]
        var += product
    # print(var)
    moment += (var - obs) ** 2
    mat_y.append(var)

mse = moment / len(test_dict)

print(mse)

# print(mat_x)
# print(mat_y)
# cor = corr(mat_x, mat_y)
# print(cor)

