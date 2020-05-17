"""
这是我们自己编写的 「决策树」 打印类

localCache class is for storing our tree data

画图基于 「turtle」库

"""


from classRef.localCache import *
from turtle import *


class Print:
    def __init__(self, typ, address, out_address=None):
        self.type = typ
        self.tree = Turtle()
        self.screen = Screen()
        self.screen.screensize(1000, 1000)
        self.ext = 1000
        tracer(0)
        self.tree.right(90)
        self.tree.penup()
        self.tree.goto(0, 480)
        self.tree.pendown()
        update()
        data = local_cache(address)
        self.mid = data['tree']
        tree_root = self.mid.root
        tracer(0)
        self.tree.pencolor('blue')
        self.tree.write(tree_root.condition + '?')
        self.tree.hideturtle()
        update()
        tracer(0)
        k = tree_root
        k.parent = None
        self.drawTree(k)
        update()
        if out_address:
            self.screen_shot = None
            self.out_address = out_address
        ontimer(self.output, 5000)
        # 画完了
        done()

    # 输出文件
    def output(self):
        self.screen_shot = getscreen()
        self.screen_shot.getcanvas().postscript(file=self.out_address)

    # 获取某节点的层数
    def getFloor(self, node):
        count = 0
        while node:
            node = node.parent
            count += 1
        return count

    # 计算间距
    def calFloor(self, n):
        return self.ext * (1/2) ** n

    # 左节点向前
    def left_forward(self, node):
        self.tree.pensize(1)
        self.tree.pencolor('blue')
        n = self.getFloor(node)
        condition = str(node.condition) + '?'
        identity = str(node.name)
        ID = str(node.ID)
        self.tree.fd(20)
        self.tree.left(90)
        self.tree.fd(self.calFloor(n))
        self.tree.right(90)
        self.tree.fd(20)
        if node.type == 'terminal':
            self.tree.pencolor('white')
            self.tree.fd(20)
            self.tree.pencolor('blue')
            if self.type == 'class':
                if node.result == 1:
                    self.tree.write('G')
                else:
                    self.tree.write('B')
                pass
            elif self.type == 'reg':
                text = node.result
                # text = '%.2f' % float(node.result)
                self.tree.write(text)
        else:
            self.tree.fd(20)
            self.tree.fd(20)
            self.tree.write(condition)

    # 左节点返回原处
    def left_back(self, node):
        n = self.getFloor(node)
        self.tree.penup()
        self.tree.right(180)
        if node.type == 'terminal':
            self.tree.fd(40)
        else:
            self.tree.fd(60)
        self.tree.left(90)
        self.tree.fd(self.calFloor(n))
        self.tree.right(90)
        self.tree.fd(20)
        self.tree.pendown()
        self.tree.right(180)

    # 右节点向前
    def right_forward(self, node):
        self.tree.pencolor('red')
        self.tree.pensize(1)
        n = self.getFloor(node)
        condition = str(node.condition) + '?'
        identity = str(node.name)
        ID = str(node.ID)
        self.tree.fd(20)
        self.tree.right(90)
        self.tree.fd(self.calFloor(n))
        self.tree.left(90)
        self.tree.fd(20)
        if node.type == 'terminal':
            self.tree.pencolor('white')
            self.tree.fd(20)
            self.tree.pencolor('red')
            if self.type == 'class':
                if node.result == 1:
                    self.tree.write('G')
                else:
                    self.tree.write('B')
                pass
            elif self.type == 'reg':
                text = node.result
                self.tree.write(text)
        else:
            self.tree.fd(20)
            self.tree.fd(20)
            self.tree.write(condition)

    # 右节点后退
    def right_back(self, node):
        n = self.getFloor(node)
        self.tree.penup()
        self.tree.left(180)
        if node.type == 'terminal':
            self.tree.fd(40)
        else:
            self.tree.fd(60)
        self.tree.right(90)
        self.tree.fd(self.calFloor(n))
        self.tree.left(90)
        self.tree.fd(20)
        self.tree.pendown()
        self.tree.left(180)

    # 总控，利用递归
    def drawTree(self, node):
        if node.left:
            self.left_forward(node.left)
            self.drawTree(node.left)
            self.left_back(node.left)
        if node.right:
            self.right_forward(node.right)
            self.drawTree(node.right)
            self.right_back(node.right)
        return


# Print('reg', 'tmp/reg/forest/551', 'result/1.eps')

