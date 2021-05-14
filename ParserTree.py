from pythonds.basic import Stack
from pythonds.trees import BinaryTree

OPERATORS = ["+", "-", "/", "^", "*"]
SYMBOLS = ["x"]


# Algorithm for ParseTree from RuneStone Academy
# https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
def ParseTree(exp):
    exp = exp.split()
    expTree = BinaryTree('')  # create an empty tree
    parents = Stack()  # create stack to hold the parents
    parents.push(expTree)  # root is kept on bttm of stack

    for item in exp:

        if item == '(':  # next item will be var or int, followed by an operator - we need to move down
            expTree.insertLeft('')  # insert empty node on left which will be a num or int later
            parents.push(expTree)
            expTree = expTree.getLeftChild()  # move down so num or var can be placed

        elif item == ')':
            expTree = parents.pop()

        elif item in OPERATORS:
            expTree.key = item  # operator is placed at current node
            expTree.insertRight('')
            parents.push(expTree)
            expTree = expTree.getRightChild()  # we move right because a symbol or an num must be placed next

        elif item not in SYMBOLS and item not in OPERATORS and item != "(" and item != ")":
            expTree.key = float(item)  # entering them as float in case anyone inputs float values
            expTree = parents.pop()

        elif item in SYMBOLS:
            expTree.key = item
            expTree = parents.pop()

    return expTree