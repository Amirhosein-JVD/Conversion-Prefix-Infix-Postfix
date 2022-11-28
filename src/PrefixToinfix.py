def isOperator(element):
    if element == '+' or element == '-' or element == '*' or element == '/' or element == '^':

        return True

    else:

        return False


def prefixToInfix(prefix):
    stack = []

    prefix = prefix[::-1]

    for i in range(len(prefix)):

        if not isOperator(prefix[i]):

            stack.append(prefix[i])

        else:

            element = "(" + stack.pop() + prefix[i] + stack.pop() + ")"

            stack.append(element)

    return stack.pop()


a = input()

print(prefixToInfix(a))