
"""
readData 是由我们自己编写的 CSV 读取程序
treeClass 是我们自己编写的 树 类
localCache 仅用来存储模型
sys 调整最大递归次数
"""

from readData import *
from classRef.treeClass import *
from classRef.localCache import *
import sys
sys.setrecursionlimit(999999)


class regGrow:
    def __init__(self, in_address, out_address=None):
        """
        :param in_address: 输入「训练数据」地址
        :param out_address:  「存储文件」地址
        """
        self.data_dict = readCSV(in_address)
        self.tree = Tree()
        self.node_count = 1
        # 是一个指标的名称
        self.pointer_name = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                             'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']
        # 所有酒的ID
        id_list = list(range(0, len(self.data_dict)))
        # Prepare a root node
        root_node = self.tree.add_root(self.node_count)
        root_node.name = 1
        root_node.ID = id_list
        # Get initial split point and corresponding pointer
        back_initial = self.pointerChoose(self.data_dict, id_list, 's')

        # 递归这个函数
        # Get started!
        self.grow(back_initial, id_list, root_node)

        # 如果要求输出，则输出数据文件。
        if out_address:
            data = local_cache(out_address)
            data['tree'] = self.tree

    def grow(self, back, id_list, node, mode=None):
        """
        利用该函数的递归特性，完成树的构建
        :param back: 上次判定的 本次「分裂指标和指标值」
        :param id_list: 流经本节点的 红酒 ID 列表
        :param node: 本节点的「父节点」
        :param mode: 模式：左或者右
        :return:
        """
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
            node.result = str(result)
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

        # 写入分裂条件
        node.condition = str(self.pointer_name[back[0]]) + '<' + str(back[1])
        # 完成

        # 左节点生长
        self.node_count += 1
        node.left = Node(self.node_count, node, None, None, None, left_division_list)
        self.tree.size += 1
        back1 = self.pointerChoose(self.data_dict, left_division_list, 'l')
        self.grow(back1, left_division_list, node.left, 'l')
        # 左节点生长完成

        # 右节点生长
        self.node_count += 1
        node.right = Node(self.node_count, node, None, None, None, right_division_list)
        self.tree.size += 1
        back2 = self.pointerChoose(self.data_dict, right_division_list, 'r')
        self.grow(back2, right_division_list, node.right, 'r')
        # 右节点生长完成
        return

    # 给定一个列表，「剔除」相同元素，并「排序」
    # 输入格式：一个列表[1, 8, 2, 2]

    def sortAndUnique(self, in_list):
        """
        :param in_list: 给定一个含有很多指标值的列表
        :return: 剔除重复值，并按大小排序
        """
        in_list = list(set(in_list))
        in_list.sort()
        return in_list

    # 输出格式：一个列表[1，2，4，6，8]
    #
    #
    #
    # 给定一个列表，返回平均值
    # 输入格式：一个列表[1, 3, 2, 3, 2]
    def average(self, in_list):
        """
        :param in_list: 任意列表
        :return: 平均值
        """
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

    # 输出格式：一个数字
    #
    #
    #
    # 计算方差
    # 输入格式：一个列表[1, 3, 2, 3, 2]
    def squareError(self, target_list):
        """
        :param target_list: 任意列表
        :return: 方差
        """
        # print(target_list)
        avg = self.average(target_list)
        delta_square_sum = 0
        for data in target_list:
            delta_square = (data - avg) ** 2
            delta_square_sum = delta_square_sum + delta_square
        return delta_square_sum

    # 输出格式： 数字
    #
    #
    # 输入格式：[某个指标的所有值]
    # 给定一个指标的所有数据，找出该指标最好的划分点
    def cutPointChoose(self, in_list):
        """
        :param in_list: 给定某个「指标」的所有可能分裂点
        :return: 找出这个指标的「最佳分割点」
        """
        # print(in_list)
        result_list = []
        # 准备切分点列表
        arith_prep = []
        for i in in_list:
            arith_prep.append(i[0])
        arith_list = self.sortAndUnique(arith_prep)
        # 对于每个切分点，做同样操作
        for cut_point in arith_list:
            target_list_small = []
            target_list_big = []
            # 按某指标的大小进行分类：大或小
            for data_pair in in_list:
                if data_pair[0] < cut_point:
                    target_list_small.append(data_pair[1])
                else:
                    target_list_big.append(data_pair[1])
            # 分别计算 mean square error
            small_delta_square = self.squareError(target_list_small)
            big_delta_square = self.squareError(target_list_big)
            # 加起来
            delta_square = small_delta_square + big_delta_square
            # 加入列表
            cut_point_delta_square_pair = [cut_point, delta_square]
            result_list.append(cut_point_delta_square_pair)
        # 找 RSS 的最小值
        result_min = None
        for result in result_list:
            if not result_min:
                result_min = result
            else:
                if result[1] <= result_min[1]:
                    result_min = result
        return result_min

    # 输出格式：[方差最小值对应的切分值, 最小的方差]
    #
    #
    # 输入：指标代码，酒的编号列表
    def getPointerData(self, pointer_num, id_list, data_dict):
        """
        :param pointer_num: 我们选定了某个指标，例如 alcohol， alcohol 代号为 10
        :param id_list: 给定酒的 ID 列表
        :param data_dict: 总数据字典
        :return: 把 这些酒的 某个指标 做成列表 并返回
        """
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

    # 返回一个含有全部 指定指标数值 的列表[1, 3, 5.5, 7.6]
    #

    # 选择本轮最优指标
    def pointerChoose(self, data_dict, id_list, mode):
        """
        :param data_dict: 流过本节点的酒 ID 列表
        :param id_list: 流过本节点的酒 ID 列表
        :param mode: 模式
        :return: 选出最佳分裂「指标」
        """
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

    #
    #
    #
    # 输入指标代码，编号列表
    def getIDData(self, pointer_num, id_list, data_dict):
        """

        :param pointer_num: 我们选定了某个指标，例如 alcohol， alcohol 代号为 10
        :param id_list: 流过本节点的酒 ID 列表
        :param data_dict: 流过本节点的酒 ID 列表
        :return:
        """
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
        """
        判断该节点内部数据是否 Pure
        :param in_list: 一个列表 [指标值， 得分值]
        :return: Bool
        """
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


# regGrow('inputData/train.csv', 'tmp/reg/treeObj')
