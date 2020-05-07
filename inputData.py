def readCSV():
    global data_dict
    # 自定义文件名
    filename = 'train.csv'
    # 列的个数
    length = 12

    # 临时存储

    data_temp = []
    for line in open(filename, 'r'):
        split_list = line.split(',')
        data_temp.append(split_list)

    i = 1
    n = len(data_temp)

    # 正式存储

    data_dict = {}

    #

    while i < n:
        this_list = data_temp[i]
        new_this_list = []
        target = this_list[length - 1]

        if "\n" in target:
            buf3 = str(this_list[length - 1])
            buf3.strip("\n")
            target = eval(buf3)
        else:
            target = eval(this_list[length - 1])

        del this_list[length - 1]

        for item in this_list:
            buf2 = eval(item)
            new_this_list.append(buf2)

        data_dict[i - 1] = [new_this_list, target]
        i = i + 1
    print(data_dict)
    return data_dict


readCSV()
