
"""
这是本 project 的主程序

regGrow 是我们自己编写的 「初级回归树」 生成类

regAsses 是我们自己编写的 「回归树评估」类

regPrune 是我们自己编写的 「回归树修剪」类

M5 是我们自己编写的 「M5' 增强算法」 类

readData 是我们自己编写的 CSV 读取程序

"""

from readData import *
from regGrow import *
from regAsses import *
from regPrune import *
from M5 import *
from compile import *
from treePrint import *


# 读取「前 80% 训练数据」
data_dict = readCSV('inputData/partial_train.csv')


# 树开始生长
print('The tree is growing, please wait a few seconds.')
T = regGrow('inputData/partial_train.csv', 'tmp/reg/treeObj')
tree = T.tree
print('Grown up!')
# 生长完成


# 初级树的评估
A = regAsses('inputData/test.csv', tree)
print('Primary tree MSE is ', A.mse)
input('Press Enter to prune the tree.')


# 开始剪枝
print('Start pruning')
stop = False
n = 1
while tree.size > 1:
    this = regPrune(tree, data_dict)
    tree = this.tree
    print('This is the', str(n), 'th pruning.')
    data = local_cache('tmp/reg/forest/' + str(n))
    data['tree'] = tree
    n = n + 1
print('Pruning is finished. All candidate trees have been stored in tmp/reg/forest')
# 剪枝完成


# 利用「后 20% 数据进行验证」
input('Press Enter to start cross validation.')
print('Cross validation starts.')
m = 1
tup_list = []
for i in range(1, n - 1):
    data = local_cache('tmp/reg/forest/' + str(m))
    tree = data['tree']
    A = regAsses('inputData/remain_train.csv', tree)
    print('This is the ', m, 'th candidate tree, MSE is', A.mse, 'R2 is', A.R2, 'Cor', A.cor)
    tup = (m, A.mse, A.R2, A.cor, A.nmse)
    tup_list.append(tup)
    m = m + 1


# 选出基于「后 20% 训练数据集」得出的 MSE 最小的「候选树」
optimal = None
for tup in tup_list:
    if not optimal:
        optimal = tup
    else:
        if tup[1] < optimal[1]:
            optimal = tup
print(optimal[0], 'th tree is the optimized tree with a MSE of ', optimal[1])
print('Cross validation ends.')


# 启用「测试数据集」，进行测试
input('Press Enter to test the model')
print('Testing begins.')
data = local_cache('tmp/reg/forest/' + str(optimal[0]))
tree = data['tree']
A = regAsses('inputData/test.csv', tree)
print(optimal[0], 'th tree is the optimal tree, MSE is', A.mse)
print('Testing finished.')


# 利用「M5' 算法」进行性能提升
input('Press Enter to apply M5 algorithm to improve our model.')
# 560 - 592 是最合理的区间，可以大大节省运算量
m5 = M5(data_dict, 560, 592)
result_list = m5.mse_list
# 选出最优化模型
min_mse = None
for tup in result_list:
    if not min_mse:
        min_mse = tup
    else:
        if tup[1] <= min_mse[1]:
            min_mse = tup
optimal_tree_id = min_mse[0]


# 基于回归树的子树，建立多个 M5 候选树，用后 20% 训练数据进行筛选
for s in result_list:
    tree = local_cache('tmp/reg/forest/' + str(s[0]))['tree']
    A = regAsses('inputData/remain_train.csv', tree)
    print('By using M5 algorithm,', s[0], 'th tree MSE is', A.mse)


# 根据 MSE 最小原理，选出最优模型，进行最终测试。
optimal = None
for tup in result_list:
    if not optimal:
        optimal = tup
    else:
        if tup[1] < optimal[1]:
            optimal = tup
print(optimal[0], 'th M5 tree is the optimized tree with a MSE of ', optimal[1])

tree = local_cache('tmp/reg/forest/' + str(optimal[0]))['tree']
A = regAsses('inputData/test.csv', tree)
print('By using M5 algorithm, final MSE is', A.mse)


# 把「最优树」编译成「python程序」
input('Press Enter to compile our model into python program...')
C = Compiler('reg', tree, 0, 'tmp/reg/regressionTreeExecution.py')
print('The python program has been saved into tmp/reg/regressionTreeExecution.py')


# 回归树的画图
input('Press Enter to draw a graph of final tree...')
D = Print('type', 'tmp/reg/forest/' + str(optimal[0]), 'tmp/reg/graph.eps')
print('The program is over.')


# 退出程序
input('Press enter to exit...')
exit()

