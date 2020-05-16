from linearReg import *
from readData import *
from classRef.localCache import *
from compile import *

tree = local_cache('tmp/reg/144')['tree']

data_dict = readCSV('inputData/partial_train.csv')

C =Compiler('reg', tree, 0, 'tmp/reg/exe.py')


def main(node):
    if node.type == 'terminal':
        R = OptRegress(node, data_dict)
        print(R.string)
        return
    else:
        if node.left:
            main(node.left)
        if node.right:
            main(node.right)
    return


main(tree.root)



