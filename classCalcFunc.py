# 我们的配置文件
from config import *


def sortAndUnique(in_list):
    in_list = list(set(in_list))
    in_list.sort()
    return in_list

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
# 输入格式：[某个指标的所有值]
# 给定一个指标的所有数据，找出该指标最好的划分点
def cutPointChoose(in_list):
    result_list = []
    # 准备切分点列表
    arith_prep = []
    for i in in_list:
        arith_prep.append(i[0])
    arith_list = sortAndUnique(arith_prep)
    # 对于每个切分点，做同样操作
    #
    #
    # gini_list = []
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
        # gini_list.append(gini)

    # print(gini_list)
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

