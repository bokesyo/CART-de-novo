# 引进计算函数

from regreCalcFunction2 import *

# 设置最大递归次数

import sys
sys.setrecursionlimit(999999)


# 导入数据

data_dict = readCSV()


# stack module
indent = -1


# 生长函数

def grow(back, id_list):
    global countsm
    global countbg
    global indent

    if back == 'ini':
        back = pointerChoose(id_list, 's')

    # 获取指标代码，获取切分点
    
    pointer = back[0]
    cut_point = back[1]

    # 获取「这一批红酒」的「该指标」列表

    data_list_by_pointer = getIDData(pointer, id_list)
    # print(id_list)

    # 判断本组数据是否「纯净」，即是否能「再分」，若纯净，就结束。

    if jufgeIfPure(data_list_by_pointer):
        result = average(getTarget(id_list))
        print(' ' * 4 * (indent + 1) + 'score = ' + str(result))
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
    indent += 1
    print(' ' * 4 * indent + 'if ' + str(pointer_name[back[0]]) + ' < ' + str(back[1]) + ':')

    # 判断这一组数据用什么「切分」最好

    back1 = pointerChoose(left_division_list, 'l')  # 获取新一轮的区分指标

    # 递归

    grow(back1, left_division_list)  # 进行新一轮生长

    # 右节点的处理

    countbg += 1  # 新的右节点

    print(' ' * 4 * indent + 'else: ')

    back2 = pointerChoose(right_division_list, 'r')  # 获取新一轮的区分指标

    grow(back2, right_division_list)  # 进行新一轮生长
    indent -= 1

#
#
#
# 开始


id_list = list(range(0, len(data_dict)))

countsm = 0
countbg = 0

grow('ini', id_list)


# 结束
#
#
#
