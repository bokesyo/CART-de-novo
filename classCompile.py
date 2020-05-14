class regCompiler:
    def __init__(self, tree, tree_id):
        self.tree = tree
        self.address = 'tmp/class/Execute_' + str(tree_id) + '.py'
        self.fh = open(self.address, "w")
        self.fh.write('')  # clear the file

        self.fh = open(self.address, "a")

        self.indent = 0
        self.node_count = 0

        self.write_header()
        self.write_body(tree.root)

    def write_header(self):
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
