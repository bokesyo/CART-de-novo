import shelve
from contextlib import closing


class local_cache:
    def __init__(self, cache='var.pkl'):
        self.cache = cache

    def __setitem__(self, key, value):
        """
        key: 变量名
        value: 变量值
        cache: 缓存名
        """
        with closing(shelve.open(self.cache, 'c')) as shelf:
            shelf[key] = value

    def __getitem__(self, key):
        """
        key : 变量名
        return：变量值
        """
        with closing(shelve.open(self.cache, 'r')) as shelf:
            return shelf[key]


# 引进计算函数


from regreCalcFunction2 import *


from treeClass import *


# 设置最大递归次数


import sys

sys.setrecursionlimit(999999)

# 导入数据

data_dict = readCSV()

print('def regtree(a):')
print('    fixed_acidity = a[0]')
print('    volatile_acidity = a[1]')
print('    citric_acid = a[2]')
print('    residual_sugar = a[3]')
print('    chlorides = a[4]')
print('    free_sulfur_dioxide = a[5]')
print('    total_sulfur_dioxide = a[6]')
print('    density = a[7]')
print('    pH = a[8]')
print('    sulphates = a[9]')
print('    alcohol = a[10]')

# stack module
indent = 0

node_count = 0
tree = Tree()


# 生长函数


def grow(back, id_list, node=None, mode=None):
    global countsm
    global countbg
    global indent
    global node_count

    if back == 'ini':
        node = tree.add_root(node_count)
        back = pointerChoose(id_list, 's')

    # 获取指标代码，获取切分点

    pointer = back[0]
    cut_point = back[1]

    # 获取「这一批红酒」的「该指标」列表

    data_list_by_pointer = getIDData(pointer, id_list)
    # print(id_list)

    # 判断本组数据是否「纯净」，即是否能「再分」，若纯净，就结束。

    if jufgeIfPure(data_list_by_pointer):
        result = average(getTarget(id_list))
        node_count += 1
        if mode == 'l':
            node.left = Node(node_count, node, None, None, result, id_list)
        elif mode == 'r':
            node.right = Node(node_count, node, None, None, result, id_list)
        print(' ' * 4 * (indent + 1) + 'return ' + str(result))
        return

    # 左节点数据表

    left_division_list = []

    # 右节点数据表

    right_division_list = []

    # 根据切分标准进行划分，小的进入左节点数据表，大的进入右节点数据表

    for item in data_list_by_pointer:
        if item[1] < cut_point:
            left_division_list.append(item[0])
        else:
            right_division_list.append(item[0])

    # 左节点的处理
    node_count += 1  # 新的左节点
    node.left = Node(node_count, node, None, None, str(pointer_name[back[0]]) + ' < ' + str(back[1]),
                     left_division_list)
    indent += 1
    print(' ' * 4 * indent + 'if ' + str(pointer_name[back[0]]) + ' < ' + str(back[1]) + ':')
    print(' ' * 4 * (indent + 1) + 'a = ' + str(left_division_list))
    # 判断这一组数据用什么「切分」最好

    back1 = pointerChoose(left_division_list, 'l')  # 获取新一轮的区分指标

    # 递归

    grow(back1, left_division_list, node.left, 'l')  # 进行新一轮生长

    # 右节点的处理

    node_count += 1  # 新的右节点
    node.right = Node(node_count, node, None, None, str(pointer_name[back[0]]) + ' >= ' + str(back[1]),
                      right_division_list)

    print(' ' * 4 * indent + 'else: ')
    print(' ' * 4 * (indent + 1) + 'a = ' + str(right_division_list))

    back2 = pointerChoose(right_division_list, 'r')  # 获取新一轮的区分指标

    grow(back2, right_division_list, node.right, 'r')  # 进行新一轮生长
    indent -= 1


#
#
#
# 开始


id_list = list(range(0, len(data_dict)))

countsm = 0
countbg = 0

grow('ini', id_list)

# 结束
#
#
#
tree_root = tree.root


from localCache import *

from turtle import *

tree = Turtle()
screen = Screen()

screensize(1000, 1000)


ext = 1000
tracer(0)
tree.right(90)
tree.penup()
tree.goto(0, 500)

tree.pendown()
update()


def getFloor(node):
    count = 0
    while node:
        node = node.parent
        count += 1
    return count


def calFloor(n):
    return ext * (1/2) ** n


def drawTree(node):
    if node.left:
        left_forward(node.left)
        drawTree(node.left)
        left_back(node.left)
    if node.right:
        right_forward(node.right)
        drawTree(node.right)
        right_back(node.right)
    return


def left_forward(node):
    tree.pensize(1)
    tree.pencolor('red')
    n = getFloor(node)
    condition = str(node.condition)
    identity = str(node.name)
    ID = str(node.ID)
    tree.fd(20)
    tree.left(90)
    tree.fd(calFloor(n))
    tree.right(90)
    tree.fd(20)
    tree.left(90)
    tree.fd(20)
    tree.right(90)
    tree.fd(40)
    tree.right(90)
    tree.fd(40)
    tree.right(90)
    tree.fd(40)
    tree.right(90)
    tree.fd(20)
    tree.right(90)
    tree.penup()
    tree.fd(20)
    tree.write(condition)
    tree.fd(20)
    tree.pendown()


def left_back(node):
    n = getFloor(node)
    tree.penup()
    tree.right(180)
    tree.fd(60)
    tree.left(90)
    tree.fd(calFloor(n))
    tree.right(90)
    tree.fd(20)
    tree.pendown()
    tree.right(180)


def right_forward(node):
    tree.pencolor('blue')
    tree.pensize(1)
    n = getFloor(node)
    condition = str(node.condition)
    identity = str(node.name)
    ID = str(node.ID)
    tree.fd(20)
    tree.right(90)
    tree.fd(calFloor(n))
    tree.left(90)
    tree.fd(20)
    tree.right(90)
    tree.fd(20)
    tree.left(90)
    tree.fd(40)
    tree.left(90)
    tree.fd(40)
    tree.left(90)
    tree.fd(40)
    tree.left(90)
    tree.fd(20)
    tree.left(90)
    tree.penup()
    tree.fd(20)
    tree.write(condition)
    tree.fd(20)
    tree.pendown()


def right_back(node):
    n = getFloor(node)
    tree.penup()
    tree.left(180)
    tree.fd(60)
    tree.right(90)
    tree.fd(calFloor(n))
    tree.left(90)
    tree.fd(20)
    tree.pendown()
    tree.left(180)


# 开始！


tracer(0)
k = tree_root

drawTree(k)

update()
ts = getscreen()

ts.getcanvas().postscript(file="duck.eps")
done()


# 结束

