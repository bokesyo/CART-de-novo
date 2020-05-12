"""

Instruction to properly use our program

1. At the very beginning, you should check the folder called inputData
This folder contains two data sets: training data (train.csv) and testing data (test.csv)
You should check if those two files are in place.

2. First you should generate a primary decision tree. Here 'primary' refers to a tree that
can make 100% correct predictions given the testing data is identical to training data.

You just run "primaryGrow.py" in the root directory

The program will generate a db file in "dataStorge" folder, called "primaryTreeObject.db"
Note that this file contains the tree object we generated in the program.
After you run the program, you won't see any visual result.

3. Secondly, if you want to see the tree graph of our decision tree, you can run "printTree.py"
After you run the program, you will see a window that contains the desired graph.
It will also generate a eps file which contains the graph in the folder "output" called treePrint.eps

4. Thirdly, if you want to generate a python program which can implement the decision tree, you can run:
"compile.py" in the root directory.
After you run the program, you will see a py file appear in the folder "output" called "generalExecute.py"

5. You can make assessment of our primary tree, you just run "assessment.py" in the root directory.
You will get a MSE (Mean Square Error) of the testing data sets.

"""