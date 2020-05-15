import time

class Tree:
    def __init__(self, value=None, trueBranch=None, falseBranch=None, results=None, col=-1, data=None):
        self.value = value # the value in this node
        self.trueBranch = trueBranch  #child
        self.falseBranch = falseBranch #child
        self.results = results #whether this node is leaf and whether is greater than 6
        self.col = col # which feature of this node
        self.data = data # the data in this node


def readData(path,start=0,length=100000): # to read data (from start to length) and store as a list 
    fil=open(path)
    datas=[]
    i=0
    for line in fil:
        if i==0:
            i += 1
            continue
        if i < start:
            i += 1
            continue
        if i > length:
            return datas
        line.replace('\n','')
        line=line.strip().split(',')
        datas.append(tuple(line))
        i+=1
    return datas


def calculateDiffCount(datas): # to count the Different datas in one dataset
    results = {} #{type1:count1, typye2:count2}
    results['<6']=0
    results['>=6']=0
    for data in datas:
        number = eval(data[-1]) #data[-1] means quality
        if number < 6:
            results['<6'] += 1
        else:
            results['>=6'] += 1
    return results


def classfier(datas): # to vote the data in one dataset
    results=calculateDiffCount(datas)
    if results['<6'] < results['>=6']:
        return True
    else:
        return False


def gini(rows): # calculate the gini in one dataset
    length = len(rows)
    if length == 0: #empty most chaos
        return 1
    results = calculateDiffCount(rows)
    imp = 0.0
    for i in results:
        imp += (results[i] / length) ** 2
    return 1 - imp


def splitDatas(rows, value, index): # split dataset into 2 lists by value and index
    list1 = []
    list2 = []
    for row in rows:
        try:
            if (eval(row[index]) >= eval(value)): #row[index] means the specific feature in one row and compare this with the value
                list1.append(row)
            else:
                list2.append(row)
            b = time.perf_counter()

        except:
            pass
    # print('list', list1, list2)
    return (list1, list2)


def buildDecisionTree(rows):
    currentSplit = gini(rows)
    # print(currentSplit)
    column_length = len(rows[0])
    rows_length = len(rows)

    best_split = 0.0 # store the best split gini

    best_value = None # the best col and its value

    best_set = None # best list1 and list2

    for col in range(column_length - 1): #different features
        col_value_set = set([line[col] for line in rows]) # different values in one feature

        for value in col_value_set: # check one by one
            # print(value)

            a = time.perf_counter()
            list1, list2 = splitDatas(rows, value, col)
            p = len(list1) / rows_length
            split = currentSplit - p * gini(list1) - (1 - p) * gini(list2) # gini of one divison

            if split > best_split:
                best_split = split
                best_value = (col, value)
                best_set = (list1, list2)


    if best_split > 0: # not over
        trueBranch = buildDecisionTree(best_set[0]) # one child and tree it
        falseBranch = buildDecisionTree(best_set[1])
        return Tree(col=best_value[0], value=eval(best_value[1]), trueBranch=trueBranch, falseBranch=falseBranch)
    else:
        print('finished')
        return Tree(results=classfier(rows), data=rows) # at the end and give a result


def classify(data, tree): # read the tree
    if tree.results != None: # leaf
        return tree.results
    else:
        branch = None
        v = eval(data[tree.col])
        if v >= tree.value:
            branch = tree.trueBranch
        else:
            branch = tree.falseBranch
        return classify(data, branch)


datas1=readData('inputData/train.csv',length=500)


datas2=readData('inputData/train.csv',start=700,length=800)


Tree=buildDecisionTree(datas1)
count=0
for data in datas2:
    g=classify(data,Tree)
    if eval(data[-1]) >= 6 and g:
        count+=1
    elif eval(data[-1]) < 6 and not g:
        count+=1
print(count)
