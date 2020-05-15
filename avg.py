from readData import *

# Import all testing data
data_dict = readCSV('inputData/test.csv')

sums = 0
n = 0
for i in data_dict:
    score = data_dict[i][1]
    sums += score
    n = n + 1

avg = sums / n

sums = 0
n = 0
for i in data_dict:
    score = data_dict[i][1]
    piece = (score - avg) ** 2
    sums += piece
    n = n + 1

avg = sums / n

print(avg)