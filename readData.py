from config import *


def readCSV(filename):

    # 自定义文件名
    # 列的个数，手动修改
    length = number_of_col
    # 读取每行，临时存储
    data_temp = []
    for line in open(filename, 'r'):
        split_list = line.split(',')
        data_temp.append(split_list)
    i = 1
    n = len(data_temp)
    # 正式存储
    data_dict = {}
    while i < n:
        this_list = data_temp[i]
        new_this_list = []

        #
        #
        # 挑出目标变量，即最后一个变量
        target = this_list[length - 1]
        if "\n" in target:
            buf3 = str(this_list[length - 1])
            buf3.strip("\n")
            target = eval(buf3)
        else:
            target = eval(this_list[length - 1])
        # 从列表删除，剩下全是自变量
        del this_list[length - 1]
        #
        #

        # 剩下自变量自成一表
        for item in this_list:
            buf2 = eval(item)
            new_this_list.append(buf2)
        # 整理数据，写入
        data_dict[i - 1] = [new_this_list, target]
        i = i + 1
    return data_dict
