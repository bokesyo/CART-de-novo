from readData import *
from predictor import *
from classRef.localCache import *
from classRef.treeClass import *


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
        self.calc()

    def calc(self):
        n = 0
        sum_delta_square = 0
        ae = 0
        for keys in self.data_dict:
            matrix = self.data_dict[keys]
            observation = matrix[1]
            prediction = self.predictor.yuce(keys)
            delta_square = (prediction - observation) ** 2
            ae_piece = abs(prediction - observation)
            sum_delta_square = sum_delta_square + delta_square
            ae += ae_piece
            n = n + 1

        mse = sum_delta_square / n
        self.mse = mse

        mae = ae / n
        self.mae = mae

        n = 0
        ac = 0
        for keys in self.data_dict:
            matrix = self.data_dict[keys]
            observation = matrix[1]
            prediction = self.predictor.yuce(keys)
            if abs(observation - prediction) < 1:
                ac += 1
            n = n + 1
        acc = ac / n

        self.rate = acc
