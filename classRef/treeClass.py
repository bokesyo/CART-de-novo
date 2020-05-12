class Node:
    def __init__(self, name = None, parent = None, left = None, right = None, condition = None, ID = [], type='node', result=''):
        self.name = name
        self.parent = parent
        self.left = left
        self.right = right
        self.condition = condition
        self.ID = ID
        self.type = type
        self.result = result

    def record_id(self,num):
        self.ID.append(num)
        return self.ID


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def add_root(self,e):
        if self.root is not None:
            print('Root already exists')
            return None
        self.size = 1
        self.root = Node(e)
        return self.root

    # 添加左子节点
    def add_left(self,p,e):
        if p.left is not None:
            print('Left child already exists')
            return None
        self.size += 1
        p.left = Node(e,p)
        return p.left

    # 添加右子节点
    def add_right(self,p,e):
        if p.right is not None:
            print('Right child already exists')
            return None
        self.size += 1
        p.right = Node(e,p)
        return p.right

    def replace(self,p,e):
        old = p.element
        p.element = e
        return old

    # 删除节点
    def delete(self,p):
        if p.parent.left is p:
            p.parent.left = None 
        if p.parent.right is p:
            p.parent.right = None 
        return p.element

    # t为root的名字,target 待定


def node_search(t,target):
    if t.name == target:
        return t
    if (t.left is None) and (t.right is None):
        return None
    else:
        if t.left is not None:
            node_search(t.left,target)
        if t.right is not None:
            node_search(t.right,target)
