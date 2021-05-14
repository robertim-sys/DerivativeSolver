from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import ParserTree
import DetermineRule


def build_tree(currentNode, dStack, newNode, nStack): # not used
    if currentNode.leftChild:
        newNode.insertLeft(currentNode.getLeftChild().key)
        if currentNode.rightChild:
            newNode.insertRight(currentNode.getRightChild().key)
            dStack.push(currentNode)
            nStack.push(newNode)
            build_tree(currentNode.getLeftChild(), dStack, newNode.getLeftChild(), nStack)
            currentNode = dStack.pop()
            innerNode = nStack.pop()
            build_tree(currentNode.getRightChild(), dStack, innerNode.getRightChild(), nStack)



def der_output(tree):
    root = tree
    outString = ''
    outString = der_output_rec(root, outString)
    return outString

def der_output_rec(currentNode, outString):
    if currentNode.leftChild:
        outString += '('
        outString = der_output_rec(currentNode.getLeftChild(), outString)
    outString += str(currentNode.key)
    if currentNode.rightChild:
        outString =der_output_rec(currentNode.getRightChild(), outString)
        outString += ')'
    return outString




