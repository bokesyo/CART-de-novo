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
        if (eval(row[index]) >= value): #row[index] means the specific feature in one row and compare this with the value
            list1.append(row)
        else:
            list2.append(row)
    return (list1, list2)


def buildDecisionTree(rows):
    currentSplit = gini(rows)
    column_length = len(rows[0])
    rows_length = len(rows)
    best_split = 0.0 # store the best split gini
    best_value = (-1,-1) # the best col and its value
    best_set = None # best list1 and list2
    for col in range(column_length - 1): #different features
        col_value_set = set([eval(line[col]) for line in rows]) # different values in one feature
        for value in col_value_set: # check one by one
            for row in rows:
                a=eval(row[col])
                b=eval(row[-1])
                area1, area2, area3, area4 = 0,0,0,0
                if a >= value and b >= 6:
                    area1 += 1
                elif a >= value and b < 6:
                    area2 += 1
                elif a < value and b >= 6:
                    area3 += 1
                else:
                    area4 += 1
            sum1 = area1 + area2
            sum2 = area3 + area4

            if area3 + area4 == 0:
                sum2 = 1
            if area1 + area2 == 0:
                sum1 = 1

            gini1 = 1 - (area1 / (sum1)) ** 2 - (area2 / (sum1)) ** 2
            gini2 = 1 - (area3 / (sum2)) ** 2 - (area4 / (sum2)) ** 2

            p = sum1 / rows_length
            split = currentSplit - p * gini1 - (1 - p) * gini2 # gini of one divison

            if split > best_split: #find better gini and store it
                best_split = split
                best_value = (col, value)

    list1, list2 = splitDatas(rows, best_value[1], best_value[0])            
    best_set = (list1, list2)
    if best_split > 0: # not over
        trueBranch = buildDecisionTree(best_set[0]) # one child and tree it
        falseBranch = buildDecisionTree(best_set[1])
        return Tree(col=best_value[0], value=best_value[1], trueBranch=trueBranch, falseBranch=falseBranch)
    else:
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


datas1=readData('inputData/train.csv',length=600)
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
