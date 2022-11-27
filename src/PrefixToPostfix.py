def isOperator(element):

    if element == '+' or element == '-' or element == '*' or element == '/' or element == '^':

        return True

    else:

        return False


def prefixToPostfix(postfix):

    stack = []

    postfix = postfix[::-1]

    for i in postfix:

        if isOperator(i):

            a = stack.pop()

            b = stack.pop()

            temp = a + b + i

            stack.append(temp)

        else:

            stack.append(i)

    for i in stack:
        print(i)


a = input()

prefixToPostfix(a)