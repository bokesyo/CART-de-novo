from classRef.localCache import *
from importData_forPeng import *

traincabinet = readCSV('inputData/partial_train.csv')
data = local_cache('tmp/regTreeObject')
tree = data['tree']


average = 0
predict_value = []
original_score = []
node_variance = []
leaf = []
for i in range(0,670):
    a = traincabinet[i]
    original_score.append(a[-1])

result = None


def node_search(t,target):
    global result
    if t.name == target:
        result = t
    if (t.left is None) and (t.right is None):
        return 
    else:
        if t.left is not None:
            node_search(t.left,target)
        if t.right is not None:
            node_search(t.right,target)


def RSST0(node):
    iter_list = node.ID
    rss = 0
    for i in iter_list:
        predict = predict_value[i] # 我需要某一瓶红酒的「预测值」
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
    for data in result_list:   #预测值列表
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


item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol','score']
start = tree.root


def clear_ID(start):
    start.ID = None
    if start.left is not None:
        clear_ID(start.left)
    elif start.right is not None:
        clear_ID(start.right)
    else:
        return tree


# 剪树同时生成新的leaf

def cut_tree(knife):
    new_result = 0
    flow_value = tree.delete(knife)

    for i in flow_value:
        new_result = new_result + original_score[i]    #提取原先所有酒的分数计算平均值
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
    global predict_value, current_node
    #cut_tree(knife)
    for i in range(0,670):   #len（dict)
        a = traincabinet[i]
        original_score.append(a[-1])
        filter(result,a)

    f = discrim(knife)
    predict_value = []
    node_variance.append((knife.name,eval('%.2f' % f)))


def main():
    global result
    for i in range(1,tree.size+1):
        if i == 1:
            pass
        else:
            #current_node = copy.deepcopy(tree.root)
            node_search(tree.root,i)
            print(i)
            if result.type != 'terminal':
                process(result)
            else:
                leaf.append(result.name)
            result = None


main()
print(node_variance)
print(leaf)
