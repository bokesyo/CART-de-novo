
from config import *
from readData import *
from classRef.localCache import *
from tmp.regExecute import *
data = local_cache(reg_tree_object)
tree = data['tree']
tree_root = tree.root
data_dict = readCSV(train_dataset)


def yuce(i):
    prep = data_dict[i][0]
    back = classifier(prep)
    return back


def guance(i):
    back = data_dict[i][1]
    return back


def RSST0(node):
    iter_list = node.ID
    rss = 0
    for i in iter_list:
        predict = yuce(i)  # 我需要某一瓶红酒的「预测值」
        observe = guance(i)  # 我需要某一瓶红酒的「观测值」
        ris = predict - observe
        ris_squ = ris ** 2
        rss += ris_squ
    return rss


def RSST1(node):
    iter_list = node.ID
    result_list = []

    for i in iter_list:
        predict = yuce(i)  # 我需要filter返回某一瓶红酒的「预测值」
        result_list.append(predict)

    sum_a = 0
    count = 0

    for i in result_list:
        sum_a = sum_a + i
        count = count + 1
    avg = sum_a / count

    delta_square_sum = 0
    for data in result_list:
        delta_square = (data - avg) ** 2
        delta_square_sum = delta_square_sum + delta_square
    return delta_square_sum


def length(node):
    if not node:
        return 0
    else:
        return length(node.left) + length(node.right) + 1


def discrim(node):
    output = (RSST1(node) - RSST0(node)) / (length(node) - 1)
    print('rss t1', RSST1(node))
    print('rss t2', RSST0(node))
    return output


a = discrim(tree.root.right.right)

print(a)

"""
如果需要某个节点的 RSS(T1) - RSS(T0) / |T0| - |T1|
直接调用 discrim(node)就返回一个值

使用前请把yuce(i) 和 guance(i) 换成自己的接口

"""



