

from classRef.localCache import *

from readData import *

from innerPredictor import *


data_dict = readCSV('inputData/remain_train.csv')

k = 1
while k < 443:
    print(k)
    data = local_cache('tmp/reg/forest/' + str(k))
    tree = data['tree']
    this_predictor = Predictor(tree, data_dict)

    n = 0
    sum_delta_square = 0
    ae = 0

    for keys in data_dict:
        matrix = data_dict[keys]
        pointer_list = matrix[0]
        observation = matrix[1]
        prediction = this_predictor.yuce(keys)

        delta_square = (prediction - observation) ** 2
        ae_piece = abs(prediction - observation)
        sum_delta_square = sum_delta_square + delta_square
        ae += ae_piece
        n = n + 1

    mse = sum_delta_square / n
    mae = ae / n

    print('The Mean Square Error of the sample is:', mse)
    print('The Mean Absolute Error of the sample is:', mae)
    k += 1

