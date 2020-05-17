

class Compiler:
    """
    这是我们自己编写的「决策树」编译器，可以把 树 object 编译成 含有一堆 if else 的 python 程序。
    """
    def __init__(self, typ, tree, tree_id=0, address='default'):
        """

        :param typ: 回归树还是分类树
        :param tree: 树 object
        :param tree_id: 编号，可指定
        :param address: 输出文件地址
        """

        self.tree = tree
        if address == 'default':
            if typ == 'class':
                self.address = 'tmp/class/exe' + str(tree_id) + '.py'
            elif typ == 'reg':
                self.address = 'tmp/reg/exe' + str(tree_id) + '.py'
        else:
            self.address = address
        # 清空现有文件
        self.fh = open(self.address, "w")
        self.fh.write('')  # clear the file

        self.fh = open(self.address, "a")
        self.indent = 0
        self.node_count = 0
        self.write_header()
        self.write_body(tree.root)

    def write_header(self):
        """

        :return: 先写入函数头
        """
        # Open an empty python file
        # Write the header
        self.fh.write('def classifier(data_list):\n')
        self.fh.write('    fixed_acidity = data_list[0]\n')
        self.fh.write('    volatile_acidity = data_list[1]\n')
        self.fh.write('    citric_acid = data_list[2]\n')
        self.fh.write('    residual_sugar = data_list[3]\n')
        self.fh.write('    chlorides = data_list[4]\n')
        self.fh.write('    free_sulfur_dioxide = data_list[5]\n')
        self.fh.write('    total_sulfur_dioxide = data_list[6]\n')
        self.fh.write('    density = data_list[7]\n')
        self.fh.write('    pH = data_list[8]\n')
        self.fh.write('    sulphates = data_list[9]\n')
        self.fh.write('    alcohol = data_list[10]\n')

    def write_body(self, node):
        """

        :param node: 给定一个节点
        :return: 如果是叶节点，写上 return，不是叶子，写上 if xxx>111 和 else
        """
        if node.type == 'terminal':
            result = node.result
            self.node_count += 1
            self.fh.write((' ' * 4 * (self.indent + 1) + 'return ' + str(result)) + '\n')
            return

        if node.left:
            self.node_count += 1
            result = node.condition
            self.indent += 1
            i = node.ID
            self.fh.write((' ' * 4 * self.indent + 'if ' + str(result) + ':') + '\n')
            self.write_body(node.left)
        else:
            pass

        if node.right:
            self.node_count += 1
            i = node.ID
            self.fh.write((' ' * 4 * self.indent + 'else: ') + '\n')
            self.write_body(node.right)
            self.indent -= 1
        else:
            pass


#
# from classRef.localCache import *
# tree = local_cache('tmp/reg/forest/551')['tree']
# C = Compiler('reg', tree, 0, 'result/1.py')


