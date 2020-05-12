from classRef.localCache import *
data = local_cache('dataStorge/primaryTreeObject')
tree = data['tree']

predict_value = []


def node_search(t, target):
    if t.name == target:
        return t
    if (t.left is None) and (t.right is None):
        return None
    else:
        if t.left is not None:
            node_search(t.left,target)
        if t.right is not None:
            node_search(t.right,target)


item = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol','score']
a=[6.7, 0.76, 0.02, 1.8, 0.078, 6.0, 12.0, 0.996, 3.55, 0.63, 9.95, 3]
pointer = tree.root


def filter(pointer):
    cut = str(pointer.condition).find('<')
    print(cut)
    value = eval(str(pointer.condition)[cut+1:])
    print(value)
    index = str(pointer.condition)[0:cut]
    print(index)

    for i in range(len(item)):
        if item[i] == index:
            break
    
    if a[i] < value:
        pointer = pointer.left
        if pointer.type == 'terminal':
            predict_value.append(pointer.result)
            return 
        else:
            filter(pointer)
    else:
        pointer = pointer.right
        if pointer.type == 'terminal':
            predict_value.append(pointer.result)
            return
        else:
            filter(pointer)

filter(pointer)
print(predict_value)