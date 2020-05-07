from treeClass import *
import random
from turtle import *

tree = Turtle()
screen = Screen()
screen.screensize(5000, 5000)

ext = 4000


def getFloor(node):
    count = 0
    while node:
        node = node.parent
        count += 1
    return count


def calFloor(n):
    return ext / 2 ** n


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
    tree.fd(5)
    tree.write(identity + '\n' + condition)
    tree.fd(35)
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
    tree.fd(5)
    tree.write(identity + '\n' + condition)
    tree.fd(35)
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


# 随便弄几个节点
a = Node()
a.condition = 'aaaa 1.1'
a.parent = None

b = Node()
b.condition = 'bbbbb, 0.44'
a.left = b
b.parent = a


c = Node()
c.condition = 'cscscsc, 9'
a.right = c
c.parent = a


d = Node()
d.condition = 'sdddd 999'
c.left = d
d.parent = c

e = Node()
e.condition = 'seeee 99'
b.right = e
e.parent = b

f = Node()
f.condition = 'seeee 99'
e.right = f
f.parent = e

g = Node()
g.condition = 'seeee 99'
f.right = g
g.parent = f

h = Node()
h.condition = 'seeee 99'
g.right = h
h.parent = g


m = Node()
m.condition = 'seeee 99'
d.left = m
m.parent = d

n = Node()
n.condition = 'seeee 99'
m.left = n
n.parent = m

o = Node()
o.condition = 'seeee 99'
n.left = o
o.parent = n

p = Node()
p.condition = 'seeee 99'
o.right = p
p.parent = o


# 开始！

tracer(0)
# 把跟节点放到函数输入
drawTree(a)

update()
done()

# 结束
