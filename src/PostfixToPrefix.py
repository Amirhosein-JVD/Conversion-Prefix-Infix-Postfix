from Functions import*
def PostfixToPrefix(exp):
    operands=[]
    for i in exp:
        if(not isOperator(i)):
            operands.append(i)
        else:
            temp=''
            temp=i+operands.pop(-2)+operands.pop(-1)
            operands.append(temp)
    return operands.pop()


