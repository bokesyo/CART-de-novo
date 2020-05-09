import shelve
from contextlib import closing

filehandle = open("execute.py", "w")
filehandle.write('')
filehandle = open("execute.py", "a")

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


filehandle.write('def classifier(data_list):\n')
filehandle.write('    fixed_acidity = data_list[0]\n')
filehandle.write('    volatile_acidity = data_list[1]\n')
filehandle.write('    citric_acid = data_list[2]\n')
filehandle.write('    residual_sugar = data_list[3]\n')
filehandle.write('    chlorides = data_list[4]\n')
filehandle.write('    free_sulfur_dioxide = data_list[5]\n')
filehandle.write('    total_sulfur_dioxide = data_list[6]\n')
filehandle.write('    density = data_list[7]\n')
filehandle.write('    pH = data_list[8]\n')
filehandle.write('    sulphates = data_list[9]\n')
filehandle.write('    alcohol = data_list[10]\n')

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
            node.left = Node(node_count, node, None, None, str(result), id_list, 'terminal')
        elif mode == 'r':
            node.right = Node(node_count, node, None, None, str(result), id_list, 'terminal')
        filehandle.write((' ' * 4 * (indent + 1) + 'return ' + str(result)) + '\n')
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
    filehandle.write((' ' * 4 * indent + 'if ' + str(pointer_name[back[0]]) + ' < ' + str(back[1]) + ':') + '\n')
    # print(' ' * 4 * (indent + 1) + 'a = ' + str(left_division_list))
    # 判断这一组数据用什么「切分」最好

    back1 = pointerChoose(left_division_list, 'l')  # 获取新一轮的区分指标

    # 递归

    grow(back1, left_division_list, node.left, 'l')  # 进行新一轮生长

    # 右节点的处理

    node_count += 1  # 新的右节点
    node.right = Node(node_count, node, None, None, str(pointer_name[back[0]]) + ' >= ' + str(back[1]),
                      right_division_list)

    filehandle.write((' ' * 4 * indent + 'else: ') + '\n')
    # print(' ' * 4 * (indent + 1) + 'a = ' + str(right_division_list))

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

filehandle.close()

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
    tree.pencolor('blue')
    n = getFloor(node)
    condition = str(node.condition)
    identity = str(node.name)
    ID = str(node.ID)
    tree.fd(20)
    tree.left(90)
    tree.fd(calFloor(n))
    tree.right(90)
    tree.fd(20)
    # 开始正方形
    #tree.left(90)
    #tree.fd(20)
    #tree.right(90)
    #tree.fd(40)
    #tree.right(90)
    #tree.fd(40)
    #tree.right(90)
    #tree.fd(40)
    #tree.right(90)
    #tree.fd(20)
    #tree.right(90)
    # 结束正方形
    #
    #tree.fd(20)
    #
    #tree.penup()


    if node.type == 'terminal':
        tree.pencolor('white')
        tree.fd(20)
        tree.pencolor('blue')
        pass
    else:
        tree.fd(20)
        tree.fd(20)
    tree.write(condition)
    #tree.pendown()


def left_back(node):
    n = getFloor(node)
    tree.penup()
    tree.right(180)
    if node.type == 'terminal':
        tree.fd(40)
    else:
        tree.fd(60)
    tree.left(90)
    tree.fd(calFloor(n))
    tree.right(90)
    tree.fd(20)
    tree.pendown()
    tree.right(180)


def right_forward(node):
    tree.pencolor('red')
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
    #
    #tree.right(90)
    #tree.fd(20)
    #tree.left(90)
    #tree.fd(40)
    #tree.left(90)
    #tree.fd(40)
    #tree.left(90)
    #tree.fd(40)
    #tree.left(90)
    #tree.fd(20)
    #tree.left(90)
    #
    #tree.fd(20)
    #
    #tree.penup()


    if node.type == 'terminal':
        tree.pencolor('white')
        tree.fd(20)
        tree.pencolor('red')
        pass
    else:
        tree.fd(20)
        tree.fd(20)
    tree.write(condition)


    #tree.pendown()


def right_back(node):
    n = getFloor(node)
    tree.penup()
    tree.left(180)
    if node.type == 'terminal':
        tree.fd(40)
    else:
        tree.fd(60)
    tree.right(90)
    tree.fd(calFloor(n))
    tree.left(90)
    tree.fd(20)
    tree.pendown()
    tree.left(180)


# 开始！

tree.hideturtle()
tracer(0)
k = tree_root
k.parent = None

drawTree(k)

update()

ts = getscreen()

ts.getcanvas().postscript(file="duck.eps")
done()


# 结束

