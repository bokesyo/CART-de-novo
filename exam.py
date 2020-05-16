from tmp.reg.test import *
from readData import *


def corr(list1, list2):
    sum_x_y = 0
    sum_x_x = 0
    sum_x = 0
    sum_y = 0
    sum_y_y = 0
    n = len(list1)
    # print('@', n)

    for j in range(0, n):
        x_y = list1[j] * list2[j]
        sum_x_y += x_y

        x_x = list1[j] ** 2
        sum_x_x += x_x

        y_y = list2[j] ** 2
        sum_y_y += y_y

        x = list1[j]
        # print(x)
        sum_x += x

        y = list2[j]
        sum_y += y

    # print(n)
    # print(sum_y)
    # print(n * sum_x ** 2)
    # print(sum_x_x)
    # print(sum_x_y)

    b = ((n * sum_x_y) - sum_x * sum_y) / (n * sum_x_x - sum_x ** 2)
    a = (sum_y - b * sum_x) / n

    r = (n * sum_x_y - sum_x * sum_y) / ((n * sum_x_x - sum_x ** 2) * (n * sum_y_y - sum_y ** 2)) ** 0.5

    return r


def main():
    data_dict = readCSV('inputData/test.csv')

    m = 0
    n = 0
    for i in data_dict:
        mat = data_dict[i][0]
        obs = data_dict[i][1]
        pre = classifier(mat)
        k = (pre - obs) ** 2
        if k < 10:
            m += k
        print(k)
        n += 1

    print(m / n)


