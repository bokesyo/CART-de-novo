from pruneClass import *

from classRef.localCache import *

from readData import *

data = local_cache('tmp/reg/regTreeObject')
tree = data['tree']

data_dict = readCSV('inputData/partial_train.csv')

print('ok')

stop = False
n = 1

while not stop:

    this = Prune(tree, data_dict)
    tree = this.tree

    # 存储模块
    data = local_cache('tmp/reg/forest/' + str(n))
    data['tree'] = tree
    #

    remain = this.tree.size
    if remain == 1:
        stop = True

    n = n + 1
