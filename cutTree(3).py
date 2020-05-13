from classRef.localCache import *
import testcabinet as x
import copy
data = local_cache('dataStorge/primaryTreeObject')
tree = data['tree']
average = 0
predict_value = []
original_score = []
node_variance = []
in_node_score = [5, 6, 8, 7, 6, 6, 7, 6, 6, 5, 5, 5, 5, 5, 5, 6, 5, 5, 6, 7, 6, 7, 6, 6, 5, 5, 5, 6, 5, 5, 6, 5, 3, 7, 8, 5, 5, 5, 5, 5, 5, 6, 6, 8, 5, 6, 6, 7, 6, 6, 6, 6, 6, 5, 6, 6, 5, 6, 5, 8, 6, 6, 6, 7, 5, 5, 5, 5, 5, 5, 6, 6, 5, 5, 8, 5, 5, 6, 5, 6, 5, 5, 6, 7, 5, 5, 6, 7, 5, 6, 6, 5, 7, 5, 6, 7, 7, 6, 5, 5, 5, 7, 5, 6, 5, 5, 5, 5, 6, 7, 5, 6, 5, 5, 6, 5, 6, 5, 5, 4, 5, 5, 6, 6, 6, 5, 7, 5, 5, 6, 5, 5, 6, 7, 7, 7, 6, 6, 6, 5, 7, 5, 5, 7, 5, 6, 6, 5, 6, 6, 6, 5, 7, 7, 6, 5, 5, 5, 5, 5, 7, 5, 6, 6, 6, 6, 5, 6, 5, 6, 7, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 5, 6, 7, 5, 7, 4, 6, 6, 5, 5, 5, 6, 6, 6, 5, 4, 5, 6, 5, 7, 5, 5, 5, 5, 5, 8, 7, 7, 6, 7, 7, 6, 6, 5, 5, 5, 6, 7, 6, 6, 6, 5, 6, 4, 6, 5, 5, 5, 5, 5, 6, 6, 5, 6, 5, 5, 5, 7, 5, 5, 6, 5, 5, 6, 6, 7, 5, 6, 6, 6, 5, 7, 7, 6, 6, 6, 7, 5, 6, 6, 6, 6, 6, 6, 5, 6, 7, 5, 6, 6, 5, 5, 7, 6, 6, 6, 5, 5, 7, 6, 5, 5, 4, 5, 5, 5, 5, 6, 5, 5, 7, 6, 6, 5, 5, 5, 6, 5, 6, 7, 5, 5, 5, 5, 7, 7, 5, 6, 4, 6, 6, 6, 6, 5, 5, 5, 5, 7, 5, 6, 7, 7, 6, 7, 5, 5, 5, 5, 6, 5, 5, 5, 6, 7, 5, 6, 5, 8, 6, 5, 5, 5, 6, 7, 5, 7, 6, 5, 6, 5, 7, 7, 6, 7, 5, 5, 5, 5, 6, 6, 7, 7, 5, 5, 5, 6, 5, 7, 5, 5, 6, 6, 5, 5, 6, 5, 5, 5, 5, 6, 5, 6, 5, 6, 5, 5, 5, 5, 6, 5, 5, 3, 6, 5, 6, 4, 5, 5, 6, 6, 6, 5, 5, 6, 5, 5, 5, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 5, 5, 6, 5, 7, 5, 5, 5, 6, 6, 6, 7, 6, 6, 5, 6, 5, 8, 5, 5, 6, 5, 6, 5, 6, 5, 5, 5, 7, 7, 6, 6, 5, 6, 5, 4, 6, 6, 4, 5, 6, 5, 5, 6, 6, 7, 6, 5, 6, 6, 6, 6, 6, 5, 5, 6, 7, 5, 6, 6, 6, 5, 6, 6, 6, 7, 6, 5, 4, 6, 5, 4, 7, 5, 6, 5, 6, 6, 5, 7, 6, 7, 4, 5, 5, 6, 6, 5, 7, 7, 6, 6, 6, 6, 5, 5, 5, 6, 6, 5, 5, 6, 6, 6, 5, 6, 5, 5, 5, 7, 7, 5, 8, 7, 5, 5, 6, 6, 6, 6, 6, 5, 4, 5, 5, 7, 6, 6, 6, 5, 6, 5, 5, 5, 7, 5, 5, 3, 5, 5, 7, 5, 5, 7, 7, 5, 5, 7, 5, 5, 5, 5, 6, 7, 7, 6, 7, 5, 6, 5, 4, 6, 5, 5, 7, 5, 5, 5, 5, 5, 5, 3, 6, 6, 6, 6, 5, 7, 6, 6, 5, 6, 5, 5, 6, 5, 6, 6, 5, 5, 6, 5, 6, 4, 5, 5, 7, 8, 6, 5, 5, 6, 7, 6, 6, 4, 5, 6, 5, 5, 7, 6, 5, 6, 6, 7, 5, 5, 5, 6, 5, 5, 5, 5, 5, 6, 5, 6, 6, 6, 5, 5, 6, 6, 6, 5, 5, 5, 6, 6, 6, 5, 6, 5, 5]
#########
####bug
#########
break_ = False
result = None

def node_search(t,target):
    global break_
    global result
    if t.name == target:
        _break = True
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



def cal_Rss(predict_value):
    RSS=0
    for i in range(len(predict_value)):
        a=(predict_value[i]-original_score[i])**2
        RSS=RSS+a
    return RSS

item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol','score']

pointer = tree.root

start = tree.root
def clear_ID(start):
    start.ID = None
    if start.left is not None:
        clear_ID(start.left)
    elif start.right is not None:
        clear_ID(start.right)
    else:
        return tree
#剪树同时生成新的leaf
def cut_tree(knife):
    new_result = 0
    flow_value = tree.delete(knife)
    for i in flow_value:
        new_result = new_result + in_node_score[i]    #提取原先所有酒的分数计算平均值
    f = new_result/len(flow_value)
    knife.result = ('%.2f' % f)
    knife.type = 'terminal'
    return knife

def filter(pointer,a):
    cut = str(pointer.condition).find('<')
    value = eval(str(pointer.condition)[cut+1:])
    index = str(pointer.condition)[0:cut]
    for i in range(len(item)):
        if item[i] == index:
            break
    if a[i] < value:
        pointer = pointer.left
        if pointer.type == 'terminal':
            predict_value.append(eval(pointer.result))
            return 
        else:
            filter(pointer,a)
    else:
        pointer = pointer.right
        if pointer.type == 'terminal':
            predict_value.append(eval(pointer.result))
            return
        else:
            filter(pointer,a)

def process(knife):
    cut_tree(knife)
    for i in range(1,449):
        a = x.testcabinet[i]
        original_score.append(a[-1])
        filter(pointer,a)
    f = cal_Rss(predict_value)
    node_variance.append((knife.name,eval('%.2f' % f)))


current_node = copy.deepcopy(tree.root)

#排除切root的可能
def continue_cut(current_node):
    process(current_node.left)
    process(current_node.right)
    target1 = current_node.left.name
    target2 = current_node.right.name
    if current_node.type != 'terminal':
        m = node_search(tree.root,2)
        m = node_search(copy.deepcopy(tree.root),target1)
        current_node1 = m
        current_node2 = node_search(copy.deepcopy(tree.root),target2)
        if current_node.left is not None:
            continue_cut(current_node1)
        if current_node.right is not None:
            continue_cut(current_node2)
#continue_cut(current_node)
#print(node_variance)
print(node_search(tree.root,2))
