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


def levelOrderList(infixExp):
    counter = 0

    max = 0

    for i in infixExp:

        if i == '(':

            counter += 1

        elif i == ')':

            counter -= 1

        if counter > max:
            max = counter

    myList = []

    for i in range(max + 1):
        temp = []

        myList.append(temp)

    myLen = len(infixExp)

    for i in range(myLen):

        myChar = infixExp[i]

        if myChar == '(':

            counter += 1

        elif myChar == ')':

            counter -= 1

        elif isOperator(myChar):

            pre = infixExp[i - 1]

            nxt = infixExp[i + 1]

            myList[counter - 1].append(myChar)

            if pre != ')':

                myList[counter].append(pre)

                if counter != max:

                    for j in range(2):
                        myList[counter + 1].append('#')

            if nxt != '(':

                myList[counter].append(nxt)

                if max != counter:

                    for j in range(2):
                        myList[counter + 1].append('#')

        res = []

        for i in range(max + 1):

            inListLen = len(myList[i])

            for j in range(inListLen):
                res.append(myList[i][j])

    return res        



def isInfix(exp):

    if((exp[0]=='(' or not isOperator(exp[0]))and(exp[-1]==')' or not isOperator(exp[-1]))):

        return True

    else:

        return False

def isPrefix(exp):

    if(isOperator(exp[0])):

        return True
    
    else:

        return False
    
def isPostfix(exp):

    if(isOperator(exp[-1])):

        return True
    
    else:

        return False
