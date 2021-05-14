from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import ParserTree
import Misc




def edit(currentNode,tree, currentTwo):
    currentNode= currentNode.getLeftChild()
    currentNode.insertLeft(currentTwo)

    print("in func")
    Misc.der_output(tree)

tree = ParserTree.ParseTree('( 5 * x )')

treetwo = ParserTree.ParseTree('( 3 * x )')
Misc.der_output(tree)
Misc.der_output((treetwo))

currentNode = tree
currentTwo = treetwo
edit(currentNode,tree, currentTwo)
print("out func")
Misc.der_output(tree)

