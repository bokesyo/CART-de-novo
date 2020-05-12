
# Import all data,
# readCSV() is written by Ruan, a member of our team
# 这是我们自己编写的数据读取程序
from readData import *

# A series of function used to calculate anything,
# and determine which pointer and criteria of splitting,
# this function is written by Xu, a member of our team
# 这是我们自己编写的计算函数
from regCalcFunc import *

# Tree class,
# This function is written by Peng, a memeber of our team
# 这是我们自己编写的树类
from classRef.treeClass import *

# Save tree object as a file
# 请注意，这个库只是用来存储变量为文件，与决策树的生长没有任何关系。
from classRef.localCache import *

# Set recursion times
# 用到了递归，调整最大递归为无限大
import sys
sys.setrecursionlimit(999999)


data_dict = readCSV('inputData/train.csv')

pointer_name = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

tree = Tree()
indent = 0
node_count = 0
countsm = 0
countbg = 0


def grow(back, id_list, node, mode=None):
    global countsm
    global countbg
    global indent
    global node_count

    pointer = back[0]
    cut_point = back[1]
    data_list_by_pointer = getIDData(pointer, id_list, data_dict)

    # 如果样本指标纯净,就成为叶子
    if jufgeIfPure(data_list_by_pointer):
        # 取平均值
        # 这是一个叶子节点
        result = average(getTarget(id_list, data_dict))
        node.condition = ''
        node.ID = id_list
        node.type = 'terminal'
        node.result = str(result)
        return

    # 如果不纯净，就继续分割
    left_division_list = []
    right_division_list = []
    for item in data_list_by_pointer:
        if item[1] < cut_point:
            left_division_list.append(item[0])
        else:
            right_division_list.append(item[0])

    node.condition = str(pointer_name[back[0]]) + '<' + str(back[1])

    node_count += 1
    node.left = Node(node_count, node, None, None, None, left_division_list)

    indent += 1

    back1 = pointerChoose(data_dict, left_division_list, 'l')
    grow(back1, left_division_list, node.left, 'l')

    node_count += 1
    node.right = Node(node_count, node, None, None, None, right_division_list)

    back2 = pointerChoose(data_dict, right_division_list, 'r')
    grow(back2, right_division_list, node.right, 'r')

    indent -= 1


# Main program
id_list = list(range(0, len(data_dict)))
# Prepare a root node
root_node = tree.add_root(node_count)
# Get initial split point and corresponding pointer
back_initial = pointerChoose(data_dict, id_list, 's')
# Get started!
grow(back_initial, id_list, root_node)

# Write database file
a = local_cache('dataStorge/primaryTreeObject')
a['tree'] = tree

