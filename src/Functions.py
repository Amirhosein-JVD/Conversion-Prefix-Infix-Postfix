def isOperator(ch):

    if ch == '+' or ch == '-' or ch == '/' or ch == '*' or ch == '^' or ch == '%':

        return True

    else:

        return False


def Precedence(operator):

    if operator == '+' or operator == '-':

        return 1

    elif operator == '*' or operator == '/':

        return 2

    elif operator == '^':

        return 4

    else:

        return 0