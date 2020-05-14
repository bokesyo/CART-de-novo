class Prune:
    def __init__(self, tree, data_dict):
        self.item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                     'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'score']
        self.tree = tree
        self.data_dict = data_dict
        # print(self.data_dict)

        self.cost_length = None

        self.node_list = {}
        self.convert(self.tree.root)
        # print(self.node_list)

        self.predict_value = None

        self.output = None
        self.weakNode()

        self.processTree()

    def convert(self, node):
        if self.length(node) == 1:
            return
        else:
            self.node_list[node.name] = node
            self.convert(node.left)
            self.convert(node.right)
        return

    def yuce(self, i):
        a = self.data_dict[i][0]
        self.filter(self.tree.root, a)
        yuce_answer = self.predict_value
        # print('yuce', yuce_answer)
        return yuce_answer

    def guance(self, i):
        guance_answer = self.data_dict[i][1]
        # print('guance', guance_answer)
        return guance_answer

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
                # print(type(pointer.result))
                prep = eval(pointer.result)

                self.predict_value = prep
                return
            else:
                self.filter(pointer, a)

    def RSST0(self, node):
        iter_list = node.ID
        rss = 0
        for i in iter_list:
            predict = self.yuce(i)
            observe = self.guance(i)
            ris = predict - observe
            ris_squ = ris ** 2
            rss += ris_squ
        return rss

    def RSST1(self, node):
        iter_list = node.ID
        result_list = []

        for i in iter_list:
            predict = self.yuce(i)
            result_list.append(predict)

        sum_a = 0
        count = 0
        # print(result_list)
        for i in result_list:
            sum_a = sum_a + i
            count = count + 1
        avg = sum_a / count

        delta_square_sum = 0
        for data in result_list:
            delta_square = (data - avg) ** 2
            delta_square_sum = delta_square_sum + delta_square
        return delta_square_sum

    def length(self, node):
        if not node:
            return 0
        else:
            return self.length(node.left) + self.length(node.right) + 1

    def discrim(self, node):
        t1 = self.RSST1(node)

        t2 = self.RSST0(node)
        t3 = self.length(node)
        self.cost_length = t3 - 1
        # print(t1, t2, t3)
        output = (t1 - t2) / (t3 - 1)
        return output

    def weakNode(self):
        node_list = self.node_list
        # print(node_list)
        disc_list = []
        for i in node_list:
            node = node_list[i]
            result = self.discrim(node)
            # print(result)
            tup = (node.name, result)
            # print(tup)
            disc_list.append(tup)

        print('<<<<<<', disc_list)

        for result in disc_list:
            if result[1] < 0:
                index_r = disc_list.index(result)
                del disc_list[index_r]

        result_min = None
        for result in disc_list:
            if not result_min:
                result_min = result
            else:
                if result[1] <= result_min[1]:
                    result_min = result
        self.output = result_min

        print(self.output, '>>>>>>')

    def processTree(self):
        node_name = self.output[0]
        node = self.node_list[node_name]

        sums = 0
        nums = 0
        for obj in node.ID:
            sums += self.yuce(obj)
            nums += 1
        avg_score = str(sums / nums)

        # print(avg_score)
        node.result = str(avg_score)
        node.condition = ''
        node.left = None
        node.right = None
        node.type = 'terminal'

        self.tree.size -= self.cost_length

