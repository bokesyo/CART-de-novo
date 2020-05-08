

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
    condition = 'NOT ' + str(node.condition)
    identity = str(node.name)
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

a = local_cache()
tree_root = a['tree_root']

tracer(0)
# 把跟节点放到函数输入
drawTree(tree_root)

update()
ts = getscreen()

ts.getcanvas().postscript(file="duck.eps")
done()




# 结束



