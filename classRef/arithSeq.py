def arithSequence(start, end):
    number = end - start
    out_list = []
    count = 0
    while count < number:
        y = start + count
        out_list.append(y)
        count += 1
    return out_list


def arithFloat(start, end, step):
    number = int((end - start) / step)
    out_list = []
    count = 0
    while count < number:
        y = start + count * step
        out_list.append(y)
        count += 1
    return out_list
