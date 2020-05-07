import time

# 已验证，无bug
# Give an Arithmetic sequence
# Divide an interval into 1000 or more sub-intervals
# 生成1000份的等差数列
# 对一个区间进行扫描
# The length of output is 1000


def arithSequence(in_list):
    max_value = max(in_list)
    min_value = min(in_list)
    step_value = (max_value - min_value) / 1000
    i_value = 1
    out_list = []
    while i_value <= 1000:
        this_value = min_value + i_value * step_value
        out_list.append(this_value)
        i_value = i_value + 1
    # print(out_list)
    return out_list


# 给定一个列表，返回平均值
def average(in_list):
    # print(in_list)
    sum_a = 0
    count = 0
    for i in in_list:
        sum_a = sum_a + i
        count = count + 1
    out_average = sum_a / count
    return out_average


# 计算差的平方
def squareError(target_list):
    # print(target_list)
    avg = average(target_list)
    delta_square_sum = 0
    for data in target_list:
        delta_square = (data - avg) ** 2
        delta_square_sum = delta_square_sum + delta_square
    return delta_square_sum


# 给定一个指标的所有数据，找出该指标最好的划分点
# in_list 的格式， [[11, 3], [10, 4], [20, 5]]
# [编号, 指标值, 目标值]
def cutPointChoose(in_list):

    result_list = []

    # 生成1000步数列
    arith_prep = []
    for i in in_list:
        arith_prep.append(i[0])
    arith_list = arithSequence(arith_prep)

    # 对于每步，做同样操作
    for cut_point in arith_list:

        target_list_small = []
        target_list_big = []

        # 按某指标的大小进行分类：大或小
        for data_pair in in_list:
            if data_pair[0] < cut_point:
                target_list_small.append(data_pair[1])
            else:
                target_list_big.append(data_pair[1])
        # print(target_list_small)
        # print(target_list_big)
        # time.sleep(0.5)
        # 分别计算 mean square error
        small_delta_square = squareError(target_list_small)
        big_delta_square = squareError(target_list_big)

        # 加起来
        delta_square = small_delta_square + big_delta_square

        # 加入列表
        cut_point_delta_square_pair = [cut_point, delta_square]
        result_list.append(cut_point_delta_square_pair)

    # 找最小的 mean square error
    result_min = None
    for result in result_list:
        if not result_min:
            result_min = result
        else:
            if result[1] <= result_min[1]:
                result_min = result

    # Final return
    return result_min

# 输出格式：[方差最小值对应的切分值, 最小的方差]
