

from classRef.localCache import *

from readData import *

from predictor import *


data_dict = readCSV('dataProcess/wine.csv')

k = 1
while k < 2:

    result_list = []
    print(k)
    data = local_cache('tmp/reg/forest/' + str(k))
    # data = local_cache('tmp/class/treeObj')
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

        result_list.append(observation)

        n = n + 1
    mse = sum_delta_square / n
    mae = ae / n

    print('The Mean Square Error of the sample is:', mse)
    print('The Mean Absolute Error of the sample is:', mae)

    in_list = result_list
    sum_a = 0
    count = 0
    for i in in_list:
        sum_a = sum_a + i
        count = count + 1
    out_average = sum_a / count

    delta_square_sum = 0
    for data in in_list:
        delta_square = (data - out_average) ** 2
        delta_square_sum = delta_square_sum + delta_square
    var = delta_square_sum / len(in_list)
    print('Variance is:', var)

    n = 0
    ac = 0

    for keys in data_dict:
        matrix = data_dict[keys]
        pointer_list = matrix[0]
        observation = matrix[1]
        prediction = this_predictor.yuce(keys)
        if abs(observation - prediction) < 1:
            ac += 1
        n = n + 1

    acc = ac / n

    print('The Accuracy is:', acc)

    k += 1


