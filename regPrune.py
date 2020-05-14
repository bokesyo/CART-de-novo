from classRef.localCache import *


for n in range(1, 100):
    data = local_cache('tmp/reg/treeObj_' + str(n - 1))
    prev_tree = data['tree']

    # 剪枝函数，得新树
    this_tree = prev_tree
    # 结束

    data = local_cache('tmp/reg/treeObj_' + str(n))
    data['tree'] = this_tree

