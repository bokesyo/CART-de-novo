
from readData import *
data_dict = readCSV('inputData/partial_train')

def filter(arg):
    pass


def RSS(node):
    if node.type == 'terminal':
        iter_list = node.ID
        for i in iter_list:
            predict = filter('xxx')  # !我需要filter返回某一瓶红酒的「预测值」
            observe = data_dict[i][1]
            ris = predict - observe
            ris_squ = ris ** 2


