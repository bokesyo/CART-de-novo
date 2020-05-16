from classRef.matrix import *

from readData import *
from classRef.localCache import *
from compile import *

data_dict = readCSV('inputData/partial_train.csv')


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
            print(beta[m][0], end=' + ')
            m += 1
            for cans in can_list:
                pointers.append(cans)
                print(beta[m][0], '*', self.item[cans], end=' + ')
                m += 1
            print()
        # else:
            # print('!!!')
        # print(pointers)

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


n = 1


def main(node):
    global n
    if node.type == 'terminal':
        # print(n)
        n += 1
        R = OptRegress(node, data_dict)
        return
    else:
        if node.left:
            main(node.left)
        if node.right:
            main(node.right)
    # print('THIS OVER')
    return


# R = OptRegress(node, data_dict)
w = 280
for k in range(2, w):
    try:
        print(k)
        node = data = local_cache('tmp/reg/forest/' + str(k))['tree'].root
        main(node)
        print('_________________________________________________________')
    except:
        pass

