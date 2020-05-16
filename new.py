from classRef.localCache import *
from treePrint import *
from readData import *
data = local_cache('tmp/reg/144')
tree = data['tree']

data_dict = readCSV('inputData/train.csv')

# Print('reg', 'tmp/reg/144')

node = tree.root.left.left

id_list = node.ID


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
