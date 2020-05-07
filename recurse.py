from regresCalc import *
from tree import *

import copy

# 数据词典初始化
data_dict = readCSV()

# 指标名称初始化
pointer_name = ['fixed acidity', 'volatile_acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']

# 编号列表初始化
id_list = list(range(0, len(data_dict)))

# 指标列表初始化
pointer_used = init_pointer(data_dict)
pointerChoose(id_list)

# 创建树根
rtree = Tree()
root = rtree.add_root('Root')
root.record_id(1)
root.condition = 'All'
root.ID = copy.deepcopy(id_list)

