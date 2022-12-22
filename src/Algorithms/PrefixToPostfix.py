def isOperator(element):

    if element == '+' or element == '-' or element == '*' or element == '/' or element == '^':

        return True

    else:

        return False


def prefixToPostfix(postfix):

    result = ""

    stack = []

    postfix = postfix[::-1]

    for i in postfix:

        if isOperator(i):

            c = stack.pop()

            b = stack.pop()

            temp = c + b + i

            stack.append(temp)

        else:

            stack.append(i)

    for i in stack:

        result += i

    return result
