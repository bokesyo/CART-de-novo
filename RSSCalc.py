
from output.generalExecute import *
# CSV reader
from readData import *


def calcRSS():
    # Import all testing data
    data_dict = readCSV('inputData/partial_train.csv')

    n = 0
    sum_delta_square = 0

    for keys in data_dict:
        matrix = data_dict[keys]
        pointer_list = matrix[0]
        observation = matrix[1]
        prediction = classifier(pointer_list)
        # print(observation, ',', prediction)
        delta_square = (prediction - observation) ** 2
        sum_delta_square = sum_delta_square + delta_square
        n = n + 1

    rss = sum_delta_square
    return rss

