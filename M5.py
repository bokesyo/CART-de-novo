from classRef.localCache import *
from predictor import *
from readData import *

def transfer(matrix):
    """
    矩阵的「转置」操作
    :param matrix:
    :return:
    """
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
    """
    矩阵的「乘法」操作
    :param mat_1:
    :param mat_2:
    :return:
    """
    res = [[0] * len(mat_2[0]) for i in range(len(mat_1))]
    for i in range(len(mat_1)):
        for j in range(len(mat_2[0])):
            for k in range(len(mat_2)):
                res[i][j] += mat_1[i][k] * mat_2[k][j]
    return res


def reverse_step0(m):
    """
    求矩阵的「逆」第零步
    :param m:
    :return:
    """
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
    """
    求矩阵的「逆」第一步
    :param m:
    :return:
    """
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
    """
    求矩阵的「逆」第二步
    :param m:
    :return:
    """
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
    """
    求矩阵的「逆」第三步
    :param m:
    :return:
    """
    n = len(m)
    l = []
    for i in range(0, n):
        l.append(m[i][i])
    return l


def reverse(matrix):
    """
    求矩阵的「逆」总控制
    :param matrix:
    :return:
    """
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


class Regress:
    def __init__(self, node, data_dict):
        self.data_dict = data_dict
        self.node = node
        self.id_list = self.node.ID
        self.beta = None
        self.regress()

    def regress(self):
        mat_x = []
        mat_y = []
        for i in self.id_list:
            X = [1] + self.data_dict[i][0]
            mat_x.append(X)
            Y = [self.data_dict[i][1]]
            mat_y.append(Y)
        # print(mat_x)
        # print(mat_y)
        if len(mat_y) == 1:
            self.beta = None
        else:
            self.beta = multiply(reverse(multiply(transfer(mat_x), mat_x)), multiply(transfer(mat_x), mat_y))


class OptRegress:
    def __init__(self, node, data_dict):
        self.item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                     'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']

        self.node = node
        self.id_list = node.ID
        self.data_dict = data_dict

        self.string = ''

        can_list = []

        for i in range(0, 11):
            r = self.process(i)
            # print(r)
            if abs(r) >= 0.01:
                can_list.append(i)
        # print('can', can_list)
        reg_dict = self.prepare(can_list)
        # print('reg dict', reg_dict)
        L = Regress(node, reg_dict)
        # print('result simple Regress',L)
        beta = L.beta
        # print('beta', beta)
        pointers = []

        m = 0
        if beta:
            self.string = self.string + str(beta[m][0]) + ' + '
            m += 1
            for cans in can_list:
                pointers.append(cans)
                self.string = self.string + str(beta[m][0]) + ' * ' + str(self.item[cans]) + ' + '
                m += 1
            self.string = self.string + '0'
            print(self.string)

    def corr(self, list1, list2):
        sum_x_y = 0
        sum_x_x = 0
        sum_x = 0
        sum_y = 0
        sum_y_y = 0
        n = len(list1)
        for j in range(0, n):
            x_y = list1[j] * list2[j]
            sum_x_y += x_y
            x_x = list1[j] ** 2
            sum_x_x += x_x
            y_y = list2[j] ** 2
            sum_y_y += y_y
            x = list1[j]
            sum_x += x
            y = list2[j]
            sum_y += y

        # print(list1, list2)

        try:
            b = ((n * sum_x_y) - sum_x * sum_y) / (n * sum_x_x - sum_x ** 2)
            a = (sum_y - b * sum_x) / n
            r = (n * sum_x_y - sum_x * sum_y) / ((n * sum_x_x - sum_x ** 2) * (n * sum_y_y - sum_y ** 2)) ** 0.5
            return r
        except:
            return 0

    def process(self, n):
        list1 = []
        list2 = []
        # print(id_list)
        for item in self.id_list:
            ob = self.data_dict[item][0]
            # print(n)
            ob_1 = ob[n]
            # print(ob_1)
            list1.append(ob_1)
            ob_2 = self.data_dict[item][1]
            list2.append(ob_2)
        r = self.corr(list1, list2)
        # print(r)
        return r

    def prepare(self, can):
        reg_list = {}
        for k in self.id_list:
            this_list = []
            for j in can:
                this = self.data_dict[k][0][j]
                this_list.append(this)
            reg_list[k] = [this_list, self.data_dict[k][1]]
        # print(reg_list)
        return reg_list


class M5:
    def __init__(self, data_dict, switch=None):
        self.data_dict = data_dict
        self.n = 1
        self.R = None
        self.P = None
        self.mse_list = []
        self.count = 1
        if not switch:
            for k in range(2, 999):

                try:
                    # Read File

                    self.tree = local_cache('tmp/reg/forest/' + str(k))['tree']
                    node = self.tree.root
                    # Process
                    self.main(node)

                    # Evaluate
                    self.evaluate()

                    # Write File
                    local_cache('tmp/reg/forest/' + str(k))['tree'] = self.tree

                except:
                    pass

    def main(self, node):
        if node.type == 'terminal':
            print(self.n)
            self.n += 1
            self.R = OptRegress(node, self.data_dict)

            # Write new result into leaf
            node.result = self.R.string

            return
        else:
            if node.left:
                self.main(node.left)
            if node.right:
                self.main(node.right)
        return

    def evaluate(self):
        self.P = Predictor(self.tree, self.data_dict)
        se = 0
        for wine in self.data_dict:
            pre = self.P.yuce(wine)
            obs = self.data_dict[wine][1]
            se += (pre - obs) ** 2
        mse = se / len(self.data_dict)
        tup = (self.count, mse)
        self.mse_list.append(tup)
        self.count += 1

    def getMSE(self):
        return self.mse_list


# tree = local_cache('tmp/reg/forest/50')['tree']
# data_dict = readCSV('inputData/partial_train.csv')
# a = Regress(tree.root.right.left.left, data_dict)
# print(a.beta)

