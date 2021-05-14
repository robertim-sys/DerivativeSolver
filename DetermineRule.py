from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import DerivativeRules
import ParserTree


def determine_rule(currentNode, currentValue, dStack):  # determines if multiplication rule or power rule for now
    rule = None

    if currentValue == 'x':
        #currentNode.key = 'y' # I was testing stuff - Leaving for now
        parent = dStack.pop()

        if parent.key == '^':
            rule = 'power'
            DerivativeRules.derivative_rule(parent, rule, dStack)


        elif parent.key == '+' or parent.key == '-':
            if determine_chain_rule(parent, dStack,):
                parent = dStack.pop()
                rule = 'chain'
                DerivativeRules.derivative_rule(parent, rule, dStack)

            if not determine_chain_rule(parent, dStack):
                rule = 'simple'
                DerivativeRules.derivative_rule(parent, rule, dStack)

        elif parent.key == '*':
            if determine_chain_rule(parent, dStack):
                parent = dStack.pop()
                rule = 'chain'
                DerivativeRules.derivative_rule(parent, rule, dStack)

            if not determine_chain_rule(parent, dStack):
                rule = 'multi'
                DerivativeRules.derivative_rule(parent, rule, dStack)

        else:  # work on other cases
            dStack.push(parent)


    elif currentValue != 'x':
        if currentNode.rightChild and currentNode.leftChild:
            rightNode = currentNode.getRightChild()
            rightValue = rightNode.key
            dStack.push(currentNode)
            determine_rule(rightNode, rightValue, dStack)
            leftNode = currentNode.getLeftChild()
            leftValue = leftNode.key
            determine_rule(leftNode, leftValue, dStack)




def determine_chain_rule(currentNode, dStack):  # far from done
    if not dStack.isEmpty():
        parent = dStack.pop()
        if parent.key == '^':
            dStack.push(parent)
            return True
        else:
            dStack.push(parent)
            return False
    else:
        return False

