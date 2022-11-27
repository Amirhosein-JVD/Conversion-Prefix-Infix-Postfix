from functions import isOperator

def postToIn(exp):
    operands=[]
    for i in exp:
        if(isOperator(i)==False):
            operands.append(i)
        else:
            temp=''
            temp='('+operands.pop(-2)+i+operands.pop(-1)+')'
            operands.append(temp)

    return operands.pop()
