from Functions import *


def infixToPrefix(exp):

    exp = exp[::-1]

    operators = []

    result = ''

    for i in exp:

        if isOperator(i):

            if len(operators) != 0 and (Precedence(i) < Precedence(operators[-1]) or (Precedence(i) == Precedence(operators[-1]) == 4)):

                result += operators.pop()

                operators.append(i)

            else:

                operators.append(i)

        elif i == ')':

            operators.append(i)

        elif i == '(':

            op = None

            while op != ')':

                op = operators.pop()

                if op == ')':
                    break

                result += op
        else:

            result += i

    while len(operators) != 0:

        result += operators.pop()

    result = result[::-1]

    return result
