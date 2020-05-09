
# Read the tree object we generated before
from classRef.localCache import *

# Use turtle to draw a tree
from turtle import *

tree = Turtle()
screen = Screen()

# Set scale
screensize(1000, 1000)
ext = 1000

# Turtle goto the top of the screen
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

    if node.type == 'terminal':
        tree.pencolor('white')
        tree.fd(20)
        tree.pencolor('blue')
        pass
    else:
        tree.fd(20)
        tree.fd(20)
    tree.write(condition)


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

    if node.type == 'terminal':
        tree.pencolor('white')
        tree.fd(20)
        tree.pencolor('red')
        pass
    else:
        tree.fd(20)
        tree.fd(20)
    tree.write(condition)


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


data = local_cache('dataStorge/primaryTreeObject')
tree_root = data['tree_root']

tree.hideturtle()
tracer(0)
k = tree_root
k.parent = None
drawTree(k)
update()

scrren_shot = getscreen()
scrren_shot.getcanvas().postscript(file="output/treePrint.eps")
done()

