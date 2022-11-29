from Functions import *


def postfixToPrefix(exp):

    operands = []

    for i in exp:

        if not isOperator(i):

            operands.append(i)

        else:

            temp = i + operands.pop(-2) + operands.pop(-1)

            operands.append(temp)

    return operands.pop()


a = input()

print(postfixToPrefix(a))
