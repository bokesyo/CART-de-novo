# Import all data
# readCSV() is written by Ruan, a member of our team
# 这是我们自己编写的数据读取程序
from readData import *
# A series of function used to calculate anything,
# and determine which pointer and criteria of splitting,
# this function is written by Xu, a member of our team
# 这是我们自己编写的计算函数
from classCalcFunc import *
# Tree class,
# This function is written by Peng, a member of our team
# 这是我们自己编写的树类
from classRef.treeClass import *
from config import *
# 引进计时函数，与决策树生长没有任何关系
# Set recursion times
# 调整最大递归为无限大
import sys
sys.setrecursionlimit(999999)


# Import all data
data_dict = readCSV('inputData/train.csv')

# Initialize tree object
tree = Tree()

node_count = 1


def grow(back, id_list, node, mode=None):
    global node_count

    pointer = back[0]
    cut_point = back[1]
    data_list_by_pointer = getIDData(pointer, id_list, data_dict)

    # If data is pure, it becomes a leaf
    # 如果样本指标纯净,就成为叶子
    if jufgeIfPure(data_list_by_pointer):
        # 这是一个叶子节点
        result = average(getTarget(id_list, data_dict))
        node.condition = ''
        node.ID = id_list
        node.type = 'terminal'
        if result >= 6:
            node.result = 1
        else:
            node.result = -1
        return

    # If data is not pure, continue splitting
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
    tree.size += 1
    back1 = pointerChoose(data_dict, left_division_list, 'l')
    grow(back1, left_division_list, node.left, 'l')

    node_count += 1
    node.right = Node(node_count, node, None, None, None, right_division_list)
    tree.size += 1
    back2 = pointerChoose(data_dict, right_division_list, 'r')
    grow(back2, right_division_list, node.right, 'r')

    return


# Main program
id_list = list(range(0, len(data_dict)))
# Prepare a root node
root_node = tree.add_root(node_count)
root_node.name = 1
root_node.ID = id_list
# Get initial split point and corresponding pointer
back_initial = pointerChoose(data_dict, id_list, 's')
# Get started!
grow(back_initial, id_list, root_node)

# 结束计时

# 以上是树的构建

# 以下是保存模型


# Save tree object as a file
# 请注意，这个库只是用来存储变量为文件，与决策树的生长没有任何关系。
from classRef.localCache import *
# Write database file
a = local_cache(class_tree_object)
a['tree'] = tree

