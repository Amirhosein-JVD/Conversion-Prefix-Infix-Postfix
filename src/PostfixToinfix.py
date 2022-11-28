from Functions import *


def postfixToInfix(exp):
    operands = []
    for i in exp:
        if not isOperator(i):
            operands.append(i)
        else:
            temp = '(' + operands.pop(-2) + i + operands.pop(-1) + ')'
            operands.append(temp)
    return operands.pop()
