
break_ = False
result = None

def node_search(t,target):
    global break_
    global result
    if t.name == target:
        _break = True
        result = t
    if (t.left is None) and (t.right is None):
        _break = True
        return
    else:
        if t.left is not None:
            if break_:
                return
            node_search(t.left,target)
        if t.right is not None:
            if break_:
                return
            node_search(t.right,target)



from classRef.localCache import *
from config import *
data = local_cache(primary_tree_object)
tlee = data['tree']
tree_root = tlee.root

node_search(tlee.root, 130)
print(result)