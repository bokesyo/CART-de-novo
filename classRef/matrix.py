def transfer(matrix):
    if not matrix:
        return matrix
    m, n = len(matrix), len(matrix[0])
    res = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(matrix[j][i])
        res.append(temp)
    return res


def multiply(mat_1, mat_2):
    res = [[0] * len(mat_2[0]) for i in range(len(mat_1))]
    for i in range(len(mat_1)):
        for j in range(len(mat_2[0])):
            for k in range(len(mat_2)):
                res[i][j] += mat_1[i][k] * mat_2[k][j]
    return res


def reverse_step0(m):
    n = len(m)
    store_list = []
    for i in range(0,n):
        store_list.append([])
        for j in range(0,n):
            if i == j:
                store_list[i].append(1)
            else:
                store_list[i].append(0)
    return store_list


def reverse_step1(m):
    global row
    n = len(m)
    swap = []
    store_list = []
    for i in range(0, n):
        swap.append(i)
        store_list.append([])
        for j in range(0, n):
            store_list[i].append(0)
    for i in range(0, n):
        max_row = m[i][i]
        row = i
        for j in range(i, n):
            if m[j][i] >= max_row:
                max_row = m[j][i]
                row = j
        swap[i] = row
        if row != i:
            for j in range(0, n):
                m[i][j], m[row][j] = m[row][j], m[i][j]
        for j in range(i+1, n):
            if m[j][i] != 0:
                store_list[j][i] = m[j][i] / m[i][i]
                for k in range(0, n):
                    m[j][k] = m[j][k] - (store_list[j][i] * m[i][k])
    return swap, m, store_list


def reverse_step2(m):
    n = len(m)
    long = len(m)-1
    store_list = []
    for i in range(0, n):
        store_list.append([])
        for j in range(0, n):
            store_list[i].append(0)

    for i in range(0, n - 1):
        for j in range(0, long-i):
            if m[long-i-j-1][long-i] != 0 and m[long-i][long-i] != 0:
                store_list[long-i-j-1][long-i] = m[long-i-j-1][long-i] / m[long-i][long-i]
                for k in range(0, n):
                    m[long-i-j-1][k] = m[long-i-j-1][k] - store_list[long-i-j-1][long-i] * m[long-i][k]
    return m, store_list


def reverse_step3(m):
    n = len(m)
    l = []
    for i in range(0, n):
        l.append(m[i][i])
    return l


def reverse(matrix):
    n = len(matrix)
    new = reverse_step0(matrix)
    (swap, matrix1, l1) = reverse_step1(matrix)
    (matrix2, l2) = reverse_step2(matrix1)
    l3 = reverse_step3(matrix2)
    for i in range(0, n):
        if swap[i] != i:
            new[i], new[swap[i]] = new[swap[i]], new[i]
        for j in range(i+1, n):
            for k in range(0, n):
                if l1[j][i] != 0:
                    new[j][k] = new[j][k] - l1[j][i] * new[i][k]
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if l2[n-1-i-j-1][n-1-i] != 0:
                for k in range(0, n):
                    new[n-1-i-j-1][k] = new[n-1-i-j-1][k] - l2[n-1-i-j-1][n-i-1] * new[n-1-i][k]
    for i in range(0, n):
        for j in range(0, n):
            new[i][j] = new[i][j] / l3[i]
    return new
