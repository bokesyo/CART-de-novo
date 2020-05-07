# 引进计算函数

from project.regreCalcFunction import *

# 设置最大递归次数

import sys
sys.setrecursionlimit(999999)

# 导入数据

data_dict = readCSV()


# 生长函数

def grow(back, id_list):
    global countsm
    global countbg

    # 获取指标代码，获取切分点
    
    pointer = back[0]
    cut_point = back[1]
    
    # 获取「这一批红酒」的「该指标」列表

    data_list_by_pointer = getIDData(pointer, id_list)
    # print(id_list)

    # 判断本组数据是否「纯净」，即是否能「再分」，若纯净，就结束。

    if jufgeIfPure(data_list_by_pointer):
        return
    
    # 左节点数据表

    left_division_list = []

    # 右节点数据表

    right_division_list = []

    # 根据切分标准进行划分，小的进入左节点数据表，大的进入右节点数据表

    for item in data_list_by_pointer:
        if item[1] < cut_point:
            left_division_list.append(item[0])
        else:
            right_division_list.append(item[0])

    # 左节点的处理

    countsm += 1  # 新的左节点
    print('{第 %' + str(countsm) + '% 个 &L& 节点开始生长', end=' ')

    # 判断这一组数据用什么「切分」最好

    back1 = pointerChoose(left_division_list)  # 获取新一轮的区分指标

    # 递归

    grow(back1, left_division_list)  # 进行新一轮生长

    print('}', end=' ')  # 本节点以下的树全部生长结束

    # 右节点的处理

    countbg += 1  # 新的右节点

    print('{第 %' + str(countbg) + '% 个 &R& 节点开始生长', end=' ')

    back2 = pointerChoose(right_division_list)  # 获取新一轮的区分指标

    grow(back2, right_division_list)  # 进行新一轮生长

    print('}', end=' ')  # 本节点以下的树全部生长结束


#
#
#
# 开始
id_list = list(range(0, len(data_dict)))

countsm = 0
countbg = 0

print('{%0% 根节点开始生长', end=' ')

back = pointerChoose(id_list)
grow(back, id_list)

print('}', end=' ')

# 结束
#
#
#
