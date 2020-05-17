class Predictor:
    """
    给定11维指标向量，给出「树」做出的预测值
    """
    def __init__(self, tree, data_dict):
        self.item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                     'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'score']
        self.tree = tree
        self.data_dict = data_dict

        self.predict_value = None
        self.predict_node = None

    def yuce(self, i):
        a = self.data_dict[i][0]
        self.filter(self.tree.root, a)
        yuce_answer = self.predict_value
        return yuce_answer

    def filter(self, pointer, a):
        """
        给定节点范围和11维向量，返回预测值！
        :param pointer:
        :param a:
        :return:
        """
        fixed_acidity = a[0]
        volatile_acidity = a[1]
        citric_acid = a[2]
        residual_sugar = a[3]
        chlorides = a[4]
        free_sulfur_dioxide = a[5]
        total_sulfur_dioxide = a[6]
        density = a[7]
        pH = a[8]
        sulphates = a[9]
        alcohol = a[10]
        cut = str(pointer.condition).find('<')
        value = eval(str(pointer.condition)[cut + 1:])
        index = str(pointer.condition)[0:cut]
        for i in range(len(self.item)):
            if self.item[i] == index:
                break
        if a[i] < value:
            pointer = pointer.left
            if pointer.type == 'terminal':
                # print(pointer.result)
                # print(type(pointer.result))
                # print(pointer.ID)
                # print(pointer.result)
                prep = eval(pointer.result)
                self.predict_value = prep
                self.predict_node = pointer
                return
            else:
                self.filter(pointer, a)
        else:
            pointer = pointer.right
            if pointer.type == 'terminal':
                # print(pointer.result)

                # print(type(pointer.result))
                # print(pointer.result)

                prep = eval(pointer.result)

                self.predict_value = prep
                self.predict_node = pointer
                return
            else:
                self.filter(pointer, a)

