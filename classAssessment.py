# Assessment Module
from config import *
# Import our implementation module
from tmp.classExecute import *
# CSV reader
from readData import *

# Import all testing data
data_dict = readCSV(assessment_dataset)

n = 0
acc = 0

for keys in data_dict:
    matrix = data_dict[keys]
    pointer_list = matrix[0]
    observation = matrix[1]
    if observation >= 6:
        ob_s = 1
    else:
        ob_s = -1

    prediction = classifier(pointer_list)
    if prediction == ob_s:
        acc +=1
    else:
        pass
    n = n + 1

rate = acc / n

print('Acurrancy is:', rate)
