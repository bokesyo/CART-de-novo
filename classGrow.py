"""
分类树的初级生长
"""

# 这是我们自己编写的数据读取程序
from readData import *
# This function is written by Peng, a member of our team
# 这是我们自己编写的树类
from classRef.treeClass import *
# 请注意，这个库只是用来存储变量为文件，与决策树的生长没有任何关系。
from classRef.localCache import *
# Set recursion times
# 调整最大递归为无限大
import sys
sys.setrecursionlimit(999999)


class classGrow:
    def __init__(self, in_address, out_address=None):
        self.data_dict = readCSV(in_address)
        self.tree = Tree()
        self.node_count = 1
        self.pointer_name = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                             'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

        id_list = list(range(0, len(self.data_dict)))
        # Prepare a root node
        root_node = self.tree.add_root(self.node_count)
        root_node.name = 1
        root_node.ID = id_list
        # Get initial split point and corresponding pointer
        back_initial = self.pointerChoose(self.data_dict, id_list, 's')

        # Get started!
        self.grow(back_initial, id_list, root_node)

        if out_address:
            data = local_cache(out_address)
            data['tree'] = self.tree

    def grow(self, back, id_list, node, mode=None):
        pointer = back[0]
        cut_point = back[1]
        data_list_by_pointer = self.getIDData(pointer, id_list, self.data_dict)

        # If data is pure, it becomes a leaf
        # 如果样本指标纯净,就成为叶子
        if self.jufgeIfPure(data_list_by_pointer):
            # 这是一个叶子节点
            result = self.average(self.getTarget(id_list, self.data_dict))
            node.condition = ''
            node.ID = id_list
            node.type = 'terminal'
            # print(result)
            if result >= 6:
                node.result = str(1)
            else:
                node.result = str(-1)
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

        node.condition = str(self.pointer_name[back[0]]) + '<' + str(back[1])

        self.node_count += 1
        node.left = Node(self.node_count, node, None, None, None, left_division_list)
        self.tree.size += 1
        back1 = self.pointerChoose(self.data_dict, left_division_list, 'l')
        self.grow(back1, left_division_list, node.left, 'l')

        self.node_count += 1
        node.right = Node(self.node_count, node, None, None, None, right_division_list)
        self.tree.size += 1
        back2 = self.pointerChoose(self.data_dict, right_division_list, 'r')
        self.grow(back2, right_division_list, node.right, 'r')

        return

    def sortAndUnique(self, in_list):
        in_list = list(set(in_list))
        in_list.sort()
        return in_list

    def average(self, in_list):
        if not in_list:
            return 0
        # print(in_list)
        sum_a = 0
        count = 0
        for i in in_list:
            sum_a = sum_a + i
            count = count + 1
        out_average = sum_a / count
        return out_average

    def cutPointChoose(self, in_list):
        result_list = []
        # 准备切分点列表
        arith_prep = []
        for i in in_list:
            arith_prep.append(i[0])
        arith_list = self.sortAndUnique(arith_prep)

        for i in arith_list:  # 候选切分点列表

            area1 = 0
            area2 = 0
            area3 = 0
            area4 = 0

            for data_pair in in_list:
                c = data_pair[0]
                b = data_pair[1]
                if c >= i and b >= 6:
                    area1 += 1
                elif c >= i and b < 6:
                    area2 += 1
                elif c < i and b >= 6:
                    area3 += 1
                else:
                    area4 += 1

            sum1 = area1 + area2
            sum2 = area3 + area4

            if area3 + area4 == 0:
                sum2 = 1
            if area1 + area2 == 0:
                sum1 = 1

            gini1 = 1 - (area1 / (sum1)) ** 2 - (area2 / (sum1)) ** 2
            gini2 = 1 - (area3 / (sum2)) ** 2 - (area4 / (sum2)) ** 2

            gini = ((sum1) / (sum1 + sum2)) * gini1 + ((sum2) / (sum1 + sum2)) * gini2
            result_list.append([i, gini])

        result_min = None
        for result in result_list:
            if not result_min:
                result_min = result
            else:
                if result[1] <= result_min[1]:
                    result_min = result
        return result_min

    def getPointerData(self, pointer_num, id_list, data_dict):
        out_list = []
        for lid in id_list:
            list_by_id = data_dict[lid]
            component = list_by_id[0]
            target = list_by_id[1]
            data_by_pointer = component[pointer_num]
            id_data = data_by_pointer
            prep = [id_data, target]
            out_list.append(prep)
        return out_list

    def pointerChoose(self, data_dict, id_list, mode):
        # 用来装入各个指标的方差的列表
        result_by_pointer_list = []
        # 生成可用指标列表
        permit_pointer = list(range(0, 11))
        # 对每个可用指标进行计算
        for pointer in permit_pointer:
            # 固定一个指标，进行方差计算
            data_list_by_pointer = self.getPointerData(pointer, id_list, data_dict)
            # 选出该指标的方差最小值对应的划分点
            # 整理数据
            result_by_pointer = [pointer] + self.cutPointChoose(data_list_by_pointer)
            # 插入总列表
            result_by_pointer_list.append(result_by_pointer)
        # 挑选最小值：最优指标 和 切分值
        # print(result_by_pointer_list)
        result_min_pointer = None
        for result_pointer in result_by_pointer_list:
            if not result_min_pointer:
                result_min_pointer = result_pointer
            else:
                if result_pointer[2] <= result_min_pointer[2]:
                    result_min_pointer = result_pointer
        return result_min_pointer
        # 返回[最小方差所对应的指标 和 对应的最小方差]

    # 输入指标代码，编号列表
    def getIDData(self, pointer_num, id_list, data_dict):
        out_list = []
        for lid in id_list:
            list_by_id = data_dict[lid]
            component = list_by_id[0]
            data_by_pointer = component[pointer_num]
            id_data = data_by_pointer

            prep = [lid, id_data]
            out_list.append(prep)
        return out_list

    # 输出[[酒的编号1， 指标值1], [酒的编号2， 指标值2]]
    #
    #
    #

    def jufgeIfPure(self, in_list):
        # print(in_list)
        my_list = []
        for item in in_list:
            my_list.append(item[1])
        for i in my_list:
            for j in my_list:
                if i != j:
                    return False
        return True
    #
    #

    #
    # 输入：指标代码，酒的编号列表
    def getTarget(self, id_list, data_dict):
        out_list = []
        for lid in id_list:
            list_by_id = data_dict[lid]
            target = list_by_id[1]
            out_list.append(target)
        return out_list
    # 返回一个含有全部 指定指标数值 的列表[1, 3, 5.5, 7.6]
    #
    #
    #


# classGrow('inputData/train.csv', 'tmp/class/treeObj')

