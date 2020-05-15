# Assessment Module

from config import *
from innerPredictor import *

# CSV reader
# 我们的数据读取程序
from readData import *

from classRef.localCache import *
data = local_cache('tmp/reg/forest/379')
tree = data['tree']

# Import all testing data
data_dict = readCSV('inputData/test.csv')

predictor = Predictor(tree, data_dict)

n = 0
sum_delta_square = 0
ae = 0

for keys in data_dict:
    matrix = data_dict[keys]
    observation = matrix[1]
    prediction = predictor.yuce(keys)
    # print(observation, ',', prediction)
    delta_square = (prediction - observation) ** 2
    ae_piece = abs(prediction - observation)
    sum_delta_square = sum_delta_square + delta_square
    ae += ae_piece
    n = n + 1


mse = sum_delta_square / n
mae = ae / n

print('The Mean Square Error of the sample is:', mse)
print('The Mean Absolute Error of the sample is:', mae)


n = 0
ac = 0

for keys in data_dict:
    matrix = data_dict[keys]
    pointer_list = matrix[0]
    observation = matrix[1]
    prediction = predictor.yuce(keys)
    if abs(observation - prediction) < 1:
        ac += 1
    n = n + 1

acc = ac / n

print('The Accuracy is:', acc)

