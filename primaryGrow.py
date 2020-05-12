
# Save tree object as a file
from classRef.localCache import *

# A series of function used to calculate anything,
# and determine which pointer and criteria of splitting,
# this function is written by Xu, a member of our team
from regCalcFunc import *

# Tree class,
# This function is written by Peng, a memeber of our team
from classRef.treeClass import *

# Set recursion times
import sys
sys.setrecursionlimit(999999)

# Open an empty python file
filehandle = open("output/primaryExecute.py", "w")
filehandle.write('')  # clear the file
filehandle = open("output/primaryExecute.py", "a")

# Write the header
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


# Import all data,
# readCSV() is written by Ruan, a member of our team
data_dict = readCSV()
pointer_name = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density', 'pH', 'sulphates', 'alcohol']


indent = 0
node_count = 0
tree = Tree()
id_list = list(range(0, len(data_dict)))
countsm = 0
countbg = 0


def grow(back, id_list, node=None, mode=None):
    global countsm
    global countbg
    global indent
    global node_count

    if back == 'ini':
        node = tree.add_root(node_count)
        back = pointerChoose(id_list, 's')

    pointer = back[0]
    cut_point = back[1]

    data_list_by_pointer = getIDData(pointer, id_list)

    if jufgeIfPure(data_list_by_pointer):
        result = average(getTarget(id_list))
        node_count += 1
        if mode == 'l':
            node.left = Node(node_count, node, None, None, str(result), id_list, 'terminal')
        elif mode == 'r':
            node.right = Node(node_count, node, None, None, str(result), id_list, 'terminal')
        filehandle.write((' ' * 4 * (indent + 1) + 'return ' + str(result)) + '\n')
        return

    left_division_list = []

    right_division_list = []

    for item in data_list_by_pointer:
        if item[1] < cut_point:
            left_division_list.append(item[0])
        else:
            right_division_list.append(item[0])

    if (left_division_list == []) and right_division_list:
        node = Node(node_count, node.parent, None, None, str(pointer_name[back[0]]) + ' >= ' + str(back[1]), right_division_list)
        back1 = pointerChoose(right_division_list, 'l')
        grow(back1, right_division_list, node, 'l')

    elif (left_division_list == []) and right_division_list:
        node = Node(node_count, node.parent, None, None, str(pointer_name[back[0]]) + ' >= ' + str(back[1]), left_division_list)
        back2 = pointerChoose(left_division_list, 'l')
        grow(back2, left_division_list, node, 'l')

    else:
        node_count += 1
        node.left = Node(node_count, node, None, None, str(pointer_name[back[0]]) + ' < ' + str(back[1]), left_division_list)
        indent += 1
        filehandle.write((' ' * 4 * indent + 'if ' + str(pointer_name[back[0]]) + ' < ' + str(back[1]) + ':') + '\n')
        back1 = pointerChoose(left_division_list, 'l')
        grow(back1, left_division_list, node.left, 'l')

        node_count += 1
        node.right = Node(node_count, node, None, None, str(pointer_name[back[0]]) + ' >= ' + str(back[1]), right_division_list)
        filehandle.write((' ' * 4 * indent + 'else: ') + '\n')
        back2 = pointerChoose(right_division_list, 'r')
        grow(back2, right_division_list, node.right, 'r')
        indent -= 1


# Main program
grow('ini', id_list)

# Write database file
tree_root = tree.root
a = local_cache('dataStorge/primaryTreeObject')
a['tree_root'] = tree_root

filehandle.close()
