class Predictor:
    def __init__(self, tree, data_dict):
        self.item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                     'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'score']
        self.tree = tree
        self.data_dict = data_dict

        self.predict_value = None

    def yuce(self, i):
        a = self.data_dict[i][0]
        self.filter(self.tree.root, a)
        yuce_answer = self.predict_value
        return yuce_answer

    def filter(self, pointer, a):
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
                prep = eval(pointer.result)

                self.predict_value = prep
                return
            else:
                self.filter(pointer, a)
        else:
            pointer = pointer.right
            if pointer.type == 'terminal':
                # print(pointer.result)

                print(type(pointer.result))
                print(pointer.result)

                prep = eval(pointer.result)

                self.predict_value = prep
                return
            else:
                self.filter(pointer, a)

