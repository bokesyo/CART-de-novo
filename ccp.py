from classRef.deepGenerate import *

from classRef.arithSeq import *
# CSV reader
from readData import *

data_dict = readCSV('inputData/train.csv')
n = 10
total = len(data_dict) - 1
# Divide into 10 patches
single_step = total // n


# Divide into 10 patches
# This is training data
def thisTrainDict(num):
    this_list_exc = arithSequence((num - 1) * single_step, num * single_step)
    this_train_dict = deepGenerate(data_dict)
    for key in this_list_exc:
        del this_train_dict[key]
    return this_train_dict


# This is corresponding testing data
def thisTestDict(num):
    this_list_exc = arithSequence((num - 1) * single_step, num * single_step)
    this_test_dict = {}
    for key in this_list_exc:
        this_test_dict[key] = data_dict[key]
    return this_test_dict


k = 1

train_dict = thisTestDict(k)
test_dict = thisTestDict(k)
range_a = arithFloat(0, 1, 0.1)

