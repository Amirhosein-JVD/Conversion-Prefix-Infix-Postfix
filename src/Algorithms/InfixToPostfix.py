def isOperator(element):

    if element == '+' or element == '-' or element == '/' or element == '*' or element == '^' or element == '%' or element == '(' or element == ')':

        return True

    else:

        return False


def getPriority(element):

    if element == '+' or element == '-':

        return 1

    if element == '*' or element == '/':

        return 2

    if element == '^':

        return 3


def infixToPostfix(infix):

    stack = []

    output = ""

    for character in infix:

        if not isOperator(character):

            output += character

        elif character == '(':

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and getPriority(character) <= getPriority(stack[-1]):

                output += stack.pop()

            stack.append(character)

    while stack:

        output += stack.pop()

    return output
