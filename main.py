from pythonds.basic import Stack
from pythonds.trees import BinaryTree
from tkinter import *
expression = ""

import Misc
import ParserTree
import DerivativeRules
import DetermineRule


def deriv(strIn):
    simpleTree = ParserTree.ParseTree(strIn)

    DerivativeRules.derivative(simpleTree)
    new = Misc.der_output(simpleTree)
    return new





def main():
    val = input("Enter your value: ")

    new = deriv(val)
    print("Derived Expression is", new)




main()







