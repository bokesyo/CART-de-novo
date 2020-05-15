from readData import *
from predictor import *
from classRef.localCache import *
from classRef.treeClass import *


class classAsses:
    def __init__(self, in_address, tree):

        self.data_dict = readCSV(in_address)
        if isinstance(tree, Tree):
            self.tree = tree
        elif isinstance(tree, str):
            mid = local_cache(tree)
            self.tree = mid['tree']
        self.predictor = Predictor(self.tree, self.data_dict)
        self.rate = None
        self.calc()

    def calc(self):
        n = 0
        acc = 0
        for keys in self.data_dict:
            matrix = self.data_dict[keys]
            observation = matrix[1]
            # print('<<<<<<<<', observation)
            if observation >= 6:
                ob_s = 1
            else:
                ob_s = -1
            prediction = self.predictor.yuce(keys)
            # print(prediction, '>>>>>>>')
            if prediction == ob_s:
                acc += 1
            else:
                pass
            n = n + 1
        self.rate = acc / n


# A = classAssess('dataProcess/test.csv', 'tmp/class/treeObj')
# print(A.rate)

