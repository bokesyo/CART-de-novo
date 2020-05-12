import time
class Tree:
    def __init__(self,value=None,trueBranch=None,falseBranch=None,results=None,attribute=-1,data=None):
        self.value=value
        self.trueBranch=trueBranch
        self.falseBranch=falseBranch
        self.results=results
        self.attribute=attribute
        self.data=data
#统计有多少高质量红酒，多少低质量，输出字典
def count(data):
    table={'High Quality':0,'Low Quality':0}
    for line in data:
        if line[-1]>6:
            table['High Quality']+=1
        else:
            table['Low Quality']+=1
    return table
#计算基尼指数
def gini(data):
    N=len(data)
    if N==0:
        return 0
    table=count(data)
    impurity=1
    for i in table:
        impurity-=(table[i]/N)**2
    return impurity
#根据某attribute小于或大于某value，切分数据   
def split(data,value,attribute):
    list1=[]
    list2=[]
    for observation in data:
        if(observation[attribute]>=value):
            list1.append(observation)
        else:
            list2.append(observation)
    return(list1,list2)
#用决策树判断某个observation属于高质量还是低质量
def decide(observation,tree):
    if tree.results:
        if tree.results['High Quality']>tree.results['Low Quality']:
            return('High Quality')
        else:
            return('Low Quality')
    if observation[tree.attribute]>=tree.value:
        return decide(observation,tree.trueBranch)
    else:
        return decide(observation,tree.falseBranch)
#测试
def test(data,tree):
    N=len(data)
    correctCount=0
    for observation in data:
        predictedType=decide(observation,tree)
        print(observation[-1],predictedType)
        if((predictedType=='High Quality')and(observation[-1]>6))or((predictedType=='Low Quality')and (observation[-1]<=6)):
            correctCount+=1
    return  correctCount/N
#构建决策树
def decisionTree(data):
    impurity=gini(data)
    columnCount=len(data[0])
    rowCount=len(data)
    mostGain=0
    outcome=None
    criteria=None
    for i in range(columnCount-1):
        columnValues=set(x[i] for x in data)
        for value in columnValues:
            list1,list2=split(data,value,i)
            p1=len(list1)/rowCount
            gain=impurity-p1*gini(list1)-(1-p1)*gini(list2)
            if gain>mostGain:
                mostGain=gain
                criteria=(i,value)
                outcome=(list1,list2)
    if mostGain>0.01:
        trueBranch=decisionTree(outcome[0]) 
        falseBranch=decisionTree(outcome[1])
        return Tree(attribute=criteria[0],value=criteria[1],trueBranch=trueBranch, falseBranch=falseBranch)
    else:
        return Tree(results=count(data),data=data)
#读取csv文档
def load(file):
    data=[]
    with open(file) as reader:
        header=next(reader)
        del header
        for line in reader:
            line=line.split(',')
            line[-1]=line[-1].strip('\n')
            data.append(line)
        data=[[float(x) for x in line]for line in data]
    return data
# 剪枝, when gain < mini Gain，合并(merge the trueBranch and the falseBranch)
def prune(tree, miniGain):
    if tree.trueBranch.results == None: prune(tree.trueBranch, miniGain)
    if tree.falseBranch.results == None: prune(tree.falseBranch, miniGain)
    if tree.trueBranch.results != None and tree.falseBranch.results != None:
        len1 = len(tree.trueBranch.data)
        len2 = len(tree.falseBranch.data)
        p = float(len1) / (len1+len2)
        gain = gini(tree.trueBranch.data + tree.falseBranch.data) - p * gini(
            tree.trueBranch.data) - (1 - p) * gini(tree.falseBranch.data)
        if (gain < miniGain):
            tree.data = tree.trueBranch.data + tree.falseBranch.data
            tree.results = count(tree.data)
            tree.trueBranch = None
            tree.falseBranch = None
def main():
    start=time.time()
    trainingSet=load('inputData/train.csv')
    tree=decisionTree(trainingSet)
    prune(tree,0.4)
    testingSet=load('inputData/test.csv')
    print("The accuracy of prediction is:",test(testingSet,tree))
    end=time.time()
    print('ruunning time:',end-start)
main()