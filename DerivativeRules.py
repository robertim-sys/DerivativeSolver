from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import ParserTree
import DetermineRule
import Misc


def derivative(tree):
    root = tree
    if root.key == '':
        root_cases(root)
    elif root.key in ParserTree.OPERATORS:  # maybe add exception error here- root must be an operator
        currentNode = tree
        currentValue = currentNode.key
        dStack = Stack()
        DetermineRule.determine_rule(currentNode, currentValue, dStack,)




def derivative_rule(parent, rule, dStack):
    if rule == 'power':
        power_rule(parent, parent.key, dStack)
        return parent
    elif rule == 'chain':
        chain_rule(parent, parent.key, dStack)
        return parent
    elif rule == 'multi':
        multi_rule(parent, parent.key, dStack)
        return parent
    elif rule == 'simple':
        simple_operation_rule(parent, parent.key, dStack)
        return parent


def root_cases(root):
    # calling the function root_cases because there is only one value in tree
    # (even if its not the root)
    leftNode = root.getLeftChild()
    leftValue = leftNode.key
    if isinstance(leftValue, float):
        root.key = 0
        root.getLeftChild().key = ''
    if leftValue in ParserTree.SYMBOLS:
        root.key = 1
        root.getLeftChild().key = ''
    root.insertRight('')


def product_rule(currentNode, currentValue, dStack):
    currentNode.Key = '/'

    gTree = currentNode.getLeftChild()
    dgTree = BinaryTree(currentNode.getLeftChild().key)
    dgNode = dgTree
    iStack = Stack()
    build_tree(currentNode.getLeftChild(), dStack, dgNode, iStack)
    dgTree = derivative(dgTree)

    fTree = currentNode.getRIghtChild()
    dfTree = BinaryTree(currentNode.getRightChild().key)
    dfNode = dfTree
    iStack = Stack()
    build_tree(currentNode.getRightChild(), dStack, dgNode, iStack)
    dfTree = derivative(dfTree)
    prodTree = BinaryTree('+')
    prodNode = quoTree
    prodNode = prodNode.getLeftChild
    prodNode.insertLeft('*')
    prodNode.insertRight('*')
    prodNode = quoNode.getRightChild
    prodNode.insertRight(dgTree)
    prodNode.insertLeft(fTree)
    prodNode = dStack.pop()
    prodNode.getLeftChild()
    prodNode.insertRight(dfTree)
    prodNode.insertLeft(gTree)
    der_output(prodNode)

def quotient_rule(currentNode, currentValue, dStack):
    currentNode.Key = '/'

    gTree = currentNode.getLeftChild()
    dgTree = BinaryTree(currentNode.getLeftChild().key)
    dgNode = dgTree
    iStack = Stack()
    build_tree(currentNode.getLeftChild(), dStack, dgNode, iStack)
    dgTree = derivative(dgTree)

    fTree = currentNode.getRIghtChild()
    dfTree = BinaryTree(currentNode.getRightChild().key)
    dfNode = dfTree
    iStack = Stack()
    build_tree(currentNode.getRightChild(), dStack, dgNode, iStack)
    dfTree = derivative(dfTree)





    quoTree = BinaryTree('/')
    quoNode = quoTree
    quoNode.insertleft('-')
    quoNode.insertRight('^')
    quoNode = quoNode.getRightChild
    quoNode.insertRight('2')
    quoNode.insertLeft(gTree)
    quoNode.getLeftChild()
    quoNode = quoNode.getLeftChild
    quoNode.insertLeft('*')
    quoNode.insertRight('*')
    quoNode = quoNode.getRightChild
    quoNode.insertRight(dgTree)
    quoNode.insertLeft(fTree)
    quoNode = dStack.pop()
    quoNode.getLeftChild()
    quoNode.insertRight(dfTree)
    quoNode.insertLeft(gTree)
    der_output(quoTree)


def chain_rule(currentNode, currentValue, dStack):
    currentNode.key = "*"
    power = currentNode.getRightChild().key

    innerTree = currentNode.getLeftChild()
    derInnerTree = BinaryTree(innerTree.key)
    derInnerNode = derInnerTree
    iStack = Stack()
    Misc.build_tree(currentNode.getLeftChild(), dStack, derInnerNode, iStack)
    derivative(derInnerTree)

    # building tree based on chain rule that will be inserted into original tree
    chainTree = BinaryTree('*')
    chainNode = chainTree
    chainNode.insertRight(derInnerTree)
    chainNode.insertLeft('*')
    chainNode = chainNode.getLeftChild()
    chainNode.insertLeft(power)
    chainNode.insertRight('^')
    chainNode = chainNode.getRightChild()
    chainNode.insertRight(power - 1)
    chainNode.insertLeft(innerTree)

    # inserting chain tree's first kids into original tree
    currentNode.insertLeft(chainTree.getLeftChild())
    currentNode.insertRight(chainTree.getRightChild())



def multi_rule(currentNode, currentValue, dStack):  # used if x is multiplied by a num (ex: 6x --> 6)
    # Note: maybe keep in multi operator, x --> 1 so students can see math behind it

    if not dStack.isEmpty():
        parent = dStack.pop()
        if parent.key == '+' or parent.key == '-':
            if isinstance(parent.getRightChild().key, float):
                parent.getRightChild().key = 0  # catches any single constant values
        dStack.push(parent)

    leftChild = currentNode.getLeftChild()
    leftValue = leftChild.key
    if leftValue == 'x':
        currentNode.getLeftChild().key = 1  # x turns to 1
    elif isinstance(leftValue, float):
        currentNode.getRightChild().key = 1  # x turns to 1



def simple_operation_rule(currentNode, currentvalue, dStack):  # idk how well this will work with complicated functions
    leftChild = currentNode.getLeftChild()
    leftValue = leftChild.key
    currentNode.getLeftChild().key = ''  #
    currentNode.getRightChild().key = ''
    currentNode.key = 1.0  # x --> 1 (really this is operator --> 1 but we want to move it up a node


def power_rule(currentNode, currentValue, dStack):
    power = currentNode.getRightChild().key
    if dStack.isEmpty():
        currentNode.key = '*'
        currentNode.getLeftChild().key = power
        dStack.push(currentNode)
        currentNode = currentNode.getRightChild()
        currentNode.key = '^'
        currentNode.insertLeft('x')
        currentNode.insertRight(power - 1)
    elif dStack.peek().key != '*':
        currentNode.key = '*'
        currentNode.getLeftChild().key = power
        dStack.push(currentNode)
        currentNode = currentNode.getRightChild()
        currentNode.key = '^'
        currentNode.insertLeft('x')
        currentNode.insertRight(power - 1)
        dStack.pop()
        dStack.pop()
    else:
        currentNode.getRightChild().key = power - 1
        currentNode = dStack.pop()
        coefficient = currentNode.getLeftChild().key
        currentNode.getLeftChild().key = coefficient * power
