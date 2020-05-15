from classRef.localCache import *
from treePrint import *
from readData import *
data = local_cache('tmp/reg/144')
tree = data['tree']

data_dict = readCSV('inputData/train.csv')

# Print('reg', 'tmp/reg/144')

node = tree.root.left.left

id_list = node.ID


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


def p(n):
    list1 = []
    list2 = []
    # print(id_list)
    for item in id_list:
        ob = data_dict[item][0]
        ob_1 = ob[n]
        list1.append(ob_1)
        ob_2 = data_dict[item][1]
        list2.append(ob_2)

    r = corr(list1, list2)
    print(r)


for i in range(0, 11):
    p(i)
