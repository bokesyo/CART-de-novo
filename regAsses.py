"""
回归树「评估」类
treeClass 是自己编写的 树 类
M5 为自己编写的 多变量线性回归 类
"""

from classRef.treeClass import *
from M5 import *
from readData import *
from classRef.localCache import *


class regAsses:
    def __init__(self, in_address, tree):
        self.data_dict = readCSV(in_address)
        if isinstance(tree, Tree):
            self.tree = tree
        elif isinstance(tree, str):
            mid = local_cache(tree)
            self.tree = mid['tree']
        self.predictor = Predictor(self.tree, self.data_dict)
        self.mse = None
        self.mae = None
        self.rate = None
        self.R2 = None
        self.R = None
        self.cor = None
        self.nmse = None
        self.calc()

    def calc(self):
        """

        :return: 计算 MSE ， MAE， Cor
        """
        n = 0
        sum_delta_square = 0
        ae = 0
        total_sum = 0

        mat_x = []
        mat_y = []

        for keys in self.data_dict:
            matrix = self.data_dict[keys]
            observation = matrix[1]
            mat_x.append(observation)
            total_sum += observation
            prediction = self.predictor.yuce(keys)
            mat_y.append(prediction)
            delta_square = (prediction - observation) ** 2
            ae_piece = abs(prediction - observation)
            sum_delta_square = sum_delta_square + delta_square
            ae += ae_piece
            n = n + 1

        mse = sum_delta_square / n
        self.mse = mse

        ssr = sum_delta_square

        mae = ae / n
        self.mae = mae

        avg = total_sum / n

        n = 0
        ac = 0
        sst = 0
        for keys in self.data_dict:
            matrix = self.data_dict[keys]
            observation = matrix[1]
            prediction = self.predictor.yuce(keys)

            sst += (observation - avg) ** 2

            if abs(observation - prediction) < 1:
               ac += 1
            n = n + 1

        R2 = 1 - ssr / sst
        R = (R2) ** 0.5
        # print(sst / n)

        self.R2 = R2
        self.R = R

        acc = ac / n

        self.rate = acc

        self.corr(mat_x, mat_y)

    def corr(self, list1, list2):
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
        self.cor = r


# tree = local_cache('tmp/reg/forest/'+str(495))['tree']
# a = regAsses('inputData/test.csv', tree)

# print(a.mse)
