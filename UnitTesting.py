import ParserTree
import DerivativeRules
import Misc


def assertEqual(result_should_be, result, test):
    if result_should_be == result:
        print(test, "test succeeded")
    else:
        print("Error", test, "test failed")


def test_simple_rule():
    test = "Simple Operation"
    simpleTree = ParserTree.ParseTree("( ( 2 * x ) + 1 ) ")
    result_should_be = "((2.0*1)+0)"
    DerivativeRules.derivative(simpleTree)
    result = Misc.der_output(simpleTree)
    assertEqual(result_should_be, result, test)


def test_multi_rule():
    test = "Multi Rule"
    multiTree = ParserTree.ParseTree("( ( 6 * x ) + ( x * 2 )")
    result_should_be = "((6.0*1)+(1*2.0))"
    DerivativeRules.derivative(multiTree)
    result = Misc.der_output(multiTree)
    assertEqual(result_should_be, result, test)


# this will fail - code needs fixing
def test_root():
    test = "Root"
    rootTree = ParserTree.ParseTree("( 24 )")  ##fix output of root tree
    result_should_be = "(0)"
    DerivativeRules.derivative(rootTree)
    result = Misc.der_output(rootTree)
    assertEqual(result_should_be, result, test)


def test_power_rule():
    test = "Power"
    powerTree = ParserTree.ParseTree("( 3 * ( x ^ 2 ) ")
    result_should_be = "(6.0*(x^1.0))"
    DerivativeRules.derivative(powerTree)
    result = Misc.der_output(powerTree)
    assertEqual(result_should_be, result, test)


def test_power_addition():
    test = "Power and Addition"
    powerAddTree = ParserTree.ParseTree("( ( x ^ 2 ) + ( x ^ 3 ) )")
    result_should_be = "((2.0*(x^1.0))+(3.0*(x^2.0)))"
    DerivativeRules.derivative(powerAddTree)
    result = Misc.der_output(powerAddTree)
    assertEqual(result_should_be, result, test)

def test_chain_rule():
    test = "Chain Rule"
    chainTree = ParserTree.ParseTree(" ( ( 2 * x ) ^ 3 ) ")
    result_should_be = "((3.0*((2.0*x)^2.0))*(2.0*1))"
    DerivativeRules.derivative(chainTree)
    result = Misc.der_output(chainTree)
    assertEqual(result_should_be, result, test)

def test_quotient_rule():
    test = "Quotient Rule"
    quoTree = ParserTree.ParseTree(" ( x ^ 2 - 3 )  / ( x ^ 2 + 1 ) ")
    result_should_be = "(((x^2.0+1.0)*(2.0x))-(x^2.0)-3.0)/(((x^2.0)+1.0)^2.0))"
    DerivativeRules.derivative(quoTree)
    result = Misc.der_output(quoTree)
    assertEqual(result_should_be, result, test)
    print(result)

test_chain_rule()
test_power_addition()
test_power_rule()
test_multi_rule()
test_simple_rule()
test_quotient_rule()