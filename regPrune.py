class regPrune:
    def __init__(self, tree, data_dict):
        """
        注意：「这里」所用的数据全都是「建树」时使用的那一部分「训练数据」，尚未使用 剩下的一部分「训练数据」。

        你好，这里的 tree 是一个 Tree Class 的实例。
        class Node:
            def __init__(self, name = None, parent = None, left = None, right = None,
                                                condition = None, ID = [], type='node', result=''):
                self.name = name
                self.parent = parent
                self.left = left
                self.right = right
                self.condition = condition
                self.ID = ID
                self.type = type
                self.result = result


        class Tree:
            def __init__(self):
                self.root = None
                self.size = 0

        data_dict 是一个数据字典，具体格式是：

        {0: [ [6.6, 0.5, 0.04, 2.1, 0.068, 6, 14, 0.9955, 3.39, 0.64, 9.4] 6 ]}
        意思是编号为 0 的红酒 它的十一个属性分别是 6.6, 0.5, 0.04, 2.1, 0.068, 6, 14, 0.9955, 3.39, 0.64, 9.4 ，实际得分为 6 分

        :param tree:
        :param data_dict:
        """

        self.item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides',
                     'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'score']

        """
        十一个指标值的名称
        """

        self.tree = tree
        self.data_dict = data_dict

        # 提前定义，无用
        self.cost_length = None
        self.predict_value = None
        self.output = None
        self.this_stop = False

        # 这里是把所有的节点全部找到，放在列表里，可以减少后续运算。
        self.node_list = {}
        self.convert(self.tree.root)

        # 第一次运行，会执行这个
        # 我们的树 over-fit 了，第一步就是把所有的「合并后不影响准确度」的节点删掉
        self.simplify()

        # 正常情况
        if not self.this_stop:
            self.weakNode()
            self.processTree()

    def simplify(self):
        """
        这就是为了把「合并后不影响准确度」的节点删掉。 没有临床价值。略过。
        :return:
        """
        node_list = self.node_list
        disc_list = []
        for i in node_list:
            node = node_list[i]
            result = self.discrim(node)
            tup = (node.name, result)
            disc_list.append(tup)

        for tup in disc_list:
            if tup[1] == 0:
                self.this_stop = True
                self.output = tup
                self.processTree()
        self.node_list = {}
        self.convert(self.tree.root)

    def convert(self, node):
        """
        把一棵树的所有节点找到，放进列表，备用。这样可以不用反复查找。略过。
        :param node:
        :return:
        """
        if self.length(node) == 1:
            return
        else:
            if (self.length(node.right) == 1) and (self.length(node.left) == 1):
                self.node_list[node.name] = node
            else:
                self.convert(node.left)
                self.convert(node.right)
        return

    def yuce(self, node, i):
        """
        给定一瓶红酒，根据「这一棵决策树」预测他的得分。
        （为了简化计算，直接从它属于的节点开始查找得分。）
        :param node:
        :param i:
        :return:
        """
        a = self.data_dict[i][0]
        self.filter(node, a)
        yuce_answer = self.predict_value
        return yuce_answer

    def guance(self, i):
        """
        给定一瓶红酒，获取他的实际得分。
        :param i:
        :return:
        """
        guance_answer = self.data_dict[i][1]
        # print('guance', guance_answer)
        return guance_answer

    def filter(self, pointer, a):
        """
        给定一个红酒 ID ，给出 预测值

        结果放在 self.predict_value 里面

        :param pointer:
        :param a:
        :return:
        """
        cut = str(pointer.condition).find('<')
        value = eval(str(pointer.condition)[cut + 1:])
        index = str(pointer.condition)[0:cut]
        for k in range(len(self.item)):
            if self.item[k] == index:
                break
        if a[k] < value:
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
        """
        如果保留这个节点，算出 RSS
        这里涉及一个公式：

        RSS(T) >= RSS(TR) + RSS(TL)


        where T is the current node


        TR is the right node
        TL is the left node

        当我们剪树时，最先被剪掉的肯定是叶节点（也就是说我们每次剪掉的也只能是叶节点，直到剪成空树！「思考 」）

        :param node:
        :return:
        """

        # 对于左节点：
        iter_list_1 = node.left.ID
        result_list = []
        # 找出这个节点里所有酒的预测值
        for i in iter_list_1:
            predict = self.yuce(node, i)
            result_list.append(predict)

        sum_a = 0
        count = 0

        # 求平均值
        for i in result_list:
            sum_a = sum_a + i
            count = count + 1
        avg = sum_a / count
        # 算出方差 = RSS 在这里是相等的
        delta_square_sum_1 = 0
        for data in result_list:
            delta_square = (data - avg) ** 2
            delta_square_sum_1 = delta_square_sum_1 + delta_square

        # 对于右节点
        iter_list_2 = node.left.ID
        result_list = []

        for i in iter_list_2:
            predict = self.yuce(node, i)
            result_list.append(predict)

        sum_a = 0
        count = 0

        for i in result_list:
            sum_a = sum_a + i
            count = count + 1
        avg = sum_a / count

        delta_square_sum_2 = 0
        for data in result_list:
            delta_square = (data - avg) ** 2
            delta_square_sum_2 = delta_square_sum_2 + delta_square

        return delta_square_sum_1 + delta_square_sum_2

    def RSST1(self, node):
        """
        如果把这个节点变成叶子，算出 RSST1
        :param node:
        :return:
        """
        iter_list = node.ID
        result_list = []

        for i in iter_list:
            predict = self.yuce(node, i)
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
        """
        算出该节点以下（包括自己）有多少个节点
        :param node:
        :return:
        """
        if not node:
            return 0
        else:
            return self.length(node.left) + self.length(node.right) + 1

    def discrim(self, node):
        """
        算出alpha = (RSST1 - RSST0) / (|T0| - |T1|)
        :param node:
        :return:
        """
        t1 = self.RSST1(node)

        t2 = self.RSST0(node)
        t3 = self.length(node)
        self.cost_length = t3 - 1
        # print(t1, t2, t3)
        output = (t1 - t2) / (t3 - 1)
        return output

    def weakNode(self):
        """
        找到 alpha 最小的节点 也就是最弱的「最没用的」那个，cut
        :return:
        """
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

        result_min = None
        for result in disc_list:
            if not result_min:
                result_min = result
            else:
                if result[1] <= result_min[1]:
                    result_min = result
        # 存储结果
        self.output = result_min

    def processTree(self):
        """
        开工，剪掉最小叶节点
        :return:
        """
        node_name = self.output[0]
        node = self.node_list[node_name]

        sums = 0
        nums = 0
        for obj in node.ID:
            sums += self.yuce(node, obj)
            nums += 1
        avg_score = str(sums / nums)

        # print(avg_score)
        node.result = str(avg_score)
        node.condition = ''
        node.left = None
        node.right = None
        node.type = 'terminal'
        print('LENGTH', self.tree.size)

        self.tree.size -= self.cost_length

    def getNewTree(self):
        """
        方便其他程序获取 「新的树」
        :return:
        """
        return self.tree

