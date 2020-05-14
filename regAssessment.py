# Assessment Module
from config import *
# Import our implementation module
from tmp.regExecute import *
# CSV reader
from readData import *

# Import all testing data
data_dict = readCSV(assessment_dataset)

n = 0
sum_delta_square = 0
ae = 0

for keys in data_dict:
    matrix = data_dict[keys]
    pointer_list = matrix[0]
    observation = matrix[1]
    prediction = classifier(pointer_list)
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

