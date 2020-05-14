from classRef.localCache import *
from importData_forPeng import *


traincabinet = readCSV('inputData/partial_train.csv')
data = local_cache('tmp/regTreeObject')
tree = data['tree']
item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol','score']
# 以上是自动导入，无需注意
# 我把 x.traincabinet 改为 traincainet, 可以直接用
tid = 0

# 将node_variance 按第二个元素从小大大排列，课本原理


def quicksort(L,low,high):
    i = low
    j = high
    if i >= j:
        return L
    pivot = L[i]
    while i<j:
        while i<j and L[j][-1]>= pivot[-1]:
            j = j-1
        L[i] = L[j]
        while i<j and L[i][-1]<=pivot[-1]:
            i = i+1
        L[j] = L[i]
    L[i] = pivot
    quicksort(L,low,i-1)
    quicksort(L,j+1,high)
    return L


average = 0
predict_value = []
original_score = []
node_variance = []
leaf = []
for i in range(0, 670):
    a = traincabinet[i]
    original_score.append(a[-1])



def RSST0(node):
    iter_list = node.ID
    rss = 0
    for i in iter_list:
        predict = predict_value[i]  # 我需要某一瓶红酒的「预测值」
        observe = original_score[i]  # 我需要某一瓶红酒的「观测值」
        ris = predict - observe
        ris_squ = ris ** 2
        rss += ris_squ
    return rss


def RSST1(node):
    iter_list = node.ID
    result_list = []
    for i in iter_list:
        predict = predict_value[i]  # 我需要filter返回某一瓶红酒的「预测值」
        result_list.append(predict)
    sum_a = 0
    count = 0
    for i in result_list:
        sum_a = sum_a + i
        count = count + 1
    avg = sum_a / count
    delta_square_sum = 0
    for data in result_list:   # 预测值列表
        delta_square = (data - avg) ** 2
        delta_square_sum = delta_square_sum + delta_square
    return delta_square_sum


def length(node):
    if not node:
        return 0
    else:
        return length(node.left) + length(node.right) + 1


def discrim(node):
    t1 = RSST1(node)
    t2 = RSST0(node)
    output = (t1 - t2) / (length(node) - 1)
    return output


# 剪树同时生成新的leaf
def cut_tree(knife):
    new_result = 0
    flow_value = tree.delete(knife)
    for i in flow_value:
        new_result = new_result + original_score[i]    # 提取原先所有酒的分数计算平均值
    f = new_result/len(flow_value)
    knife.result = ('%.2f' % f)
    knife.type = 'terminal'
    return knife


def filter(pointer, a):
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
            filter(pointer, a)
    else:
        pointer = pointer.right
        if pointer.type == 'terminal':
            predict_value.append(eval(pointer.result))
            return
        else:
            filter(pointer, a)


def process(knife):
    global predict_value, current_node
    for i in range(0, 670):   # len（dict)
        a = traincabinet[i]
        original_score.append(a[-1])
        filter(result, a)
    f = discrim(knife)
    predict_value = []
    node_variance.append((knife.name, eval('%.2f' % f)))


def one_round():
    global tid
    global result
    tid += 1
    for i in range(1, 888):
        # print(i)
        node_search(tree.root, i)
        if not result:
            continue
        if result.type != 'terminal':
            process(result)
        else:
            leaf.append(result.name)
        result = None


def cut_auto():
    global tid
    global node_variance,result
    one_round()
    while len(node_variance) != 0:
        print('######',len(node_variance),'######')
        quicksort(node_variance,0,len(node_variance)-1)
        node_search(tree.root,node_variance[0][0])
        print(node_variance[0])
        print('tree size1',tree.size)
        print('****',length(result))
        decrease_size = length(result)-1
        cut_tree(result)
        node_variance = []


    ####以上代码将剪掉上一轮相关性最小的节点，可在此插入存储树的代码

        data = local_cache('tmp/regTreeObject' + str(tid))
        data['tree'] = tree

    ####以下为新一轮剪枝前的计算

        tree.size -= decrease_size
        print('tree size2',tree.size)
        result = None
        one_round()

    print('Done')

cut_auto()


