def isOperator(ch):
    if ch == '+' or ch == '-' or ch == '/' or ch == '*' or ch == '^' or ch == '%':
        return True
    else:
        return False


def postfixToInfix(exp):

    operands = []
    for i in exp:
        if not isOperator(i):
            operands.append(i)
        else:
            temp = '(' + operands.pop(-2) + i + operands.pop(-1) + ')'
            operands.append(temp)

    return operands.pop()
