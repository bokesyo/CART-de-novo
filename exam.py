from linearReg import *
from readData import *
from classRef.localCache import *
from compile import *

tree = local_cache('tmp/reg/forest/108')['tree']

data_dict = readCSV('inputData/partial_train.csv')

C = Compiler('reg', tree, 0, 'tmp/reg/exe.py')


n = 0


def main(node):
    global n
    if node.type == 'terminal':
        n += 1
        R = Regress(node, data_dict)
        print(n)
        print(R.beta)
        return
    else:
        if node.left:
            main(node.left)
        if node.right:
            main(node.right)
    return


# main(tree.root)

R = Regress(tree.root, data_dict)
print(R.beta)


