# 我们的配置文件
from config import *

# 给定一个列表，「剔除」相同元素，并「排序」
# 输入格式：一个列表[1, 8, 2, 2]


def sortAndUnique(in_list):
    in_list = list(set(in_list))
    in_list.sort()
    return in_list
# 输出格式：一个列表[1，2，4，6，8]
#
#
#


#
#
#
# 给定一个列表，返回平均值
# 输入格式：一个列表[1, 3, 2, 3, 2]
def average(in_list):
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


#
#
#
# 计算方差
# 输入格式：一个列表[1, 3, 2, 3, 2]
def squareError(target_list):
    # print(target_list)
    avg = average(target_list)
    delta_square_sum = 0
    for data in target_list:
        delta_square = (data - avg) ** 2
        delta_square_sum = delta_square_sum + delta_square
    return delta_square_sum
# 输出格式： 数字
#
#
#


#
#
#
# 输入格式：[某个指标的所有值]
# 给定一个指标的所有数据，找出该指标最好的划分点
def cutPointChoose(in_list):
    # print(in_list)
    result_list = []
    # 准备切分点列表
    arith_prep = []
    for i in in_list:
        arith_prep.append(i[0])
    arith_list = sortAndUnique(arith_prep)
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
        small_delta_square = squareError(target_list_small)
        big_delta_square = squareError(target_list_big)
        # 加起来
        delta_square = small_delta_square + big_delta_square
        # 加入列表
        cut_point_delta_square_pair = [cut_point, delta_square]
        result_list.append(cut_point_delta_square_pair)
    # 找最小值
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
#


#
#
#
# 输入：指标代码，酒的编号列表
def getPointerData(pointer_num, id_list, data_dict):
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
#
#


#
#
#
# 选择本轮最优指标
def pointerChoose(data_dict, id_list, mode):
    # 用来装入各个指标的方差的列表
    result_by_pointer_list = []
    # 生成可用指标列表
    permit_pointer = list(range(0, number_of_col - 1))
    # 对每个可用指标进行计算
    for pointer in permit_pointer:
        # 固定一个指标，进行方差计算
        data_list_by_pointer = getPointerData(pointer, id_list, data_dict)
        # 选出该指标的方差最小值对应的划分点
        # 整理数据
        result_by_pointer = [pointer] + cutPointChoose(data_list_by_pointer)
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
def getIDData(pointer_num, id_list, data_dict):
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


def jufgeIfPure(in_list):
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


#
#
#
# 输入：指标代码，酒的编号列表
def getTarget(id_list, data_dict):
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


