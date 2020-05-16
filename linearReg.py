from classRef.matrix import *


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
        self.beta = multiply(reverse(multiply(transfer(mat_x), mat_x)), multiply(transfer(mat_x), mat_y))


class OptRegress:
    def __init__(self, node, data_dict):
        self.item = ['1', 'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                     'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'score']
        self.node = node
        self.id_list = node.ID
        self.data_dict = data_dict

        can_list = []

        for i in range(0, 11):
            r = self.process(i)
            # print(r)
            if abs(r) >= 0.1:
                can_list.append(i)

        reg_dict = self.prepare(can_list)
        L = Regress(node, reg_dict)
        beta = L.beta
        # print(beta)
        pointers = []
        for cans in can_list:
            pointers.append(cans + 1)
        # print(pointers)
        string_h = ''
        for ct in range(0, len(pointers)):
            if ct == len(pointers) - 1:
                string_h = string_h + self.item[pointers[ct]] + ' * ' + str(beta[ct][0])
            else:
                string_h = string_h + self.item[pointers[ct]] + ' * ' + str(beta[ct][0]) + ' + '
        string = str(beta[0][0]) + ' + ' + string_h
        self.string = string
        # print(string)

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
        b = ((n * sum_x_y) - sum_x * sum_y) / (n * sum_x_x - sum_x ** 2)
        a = (sum_y - b * sum_x) / n

        # print(n)
        # print(sum_x, 'sumx')
        # print(sum_x_x, 'sumxx')
        # print(sum_y, 'sumy')
        # print(sum_y_y, 'sumyy')
        # print(sum_x_y, 'sumxy')

        if sum_y == n * y:
            return 0
        r = (n * sum_x_y - sum_x * sum_y) / ((n * sum_x_x - sum_x ** 2) * (n * sum_y_y - sum_y ** 2)) ** 0.5
        return r

    def process(self, n):
        list1 = []
        list2 = []
        # print(id_list)
        for item in self.id_list:
            ob = self.data_dict[item][0]
            ob_1 = ob[n]
            list1.append(ob_1)
            ob_2 = self.data_dict[item][1]
            list2.append(ob_2)
        r = self.corr(list1, list2)
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

