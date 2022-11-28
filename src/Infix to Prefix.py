from Functions import*

def InfixToPrefix(exp):
    exp=exp[::-1]
    operators=[]
    rslt=''
    for i in exp:
        if(isOperator(i)):
            if(len(operators)!=0 and (Precedence(i)<Precedence(operators[-1])or(Precedence(i)==Precedence(operators[-1])==4))):
                rslt+=operators.pop()
                operators.append(i)
            else:
                operators.append(i)
        elif(i==')'):operators.append(i)
        elif(i=='('):
            op=None
            while(op!=')'):
                op=operators.pop()
                if(op==')'):break
                rslt+=op
        else:
            rslt+=i
    while(len(operators)!=0):
        rslt+=operators.pop()
    rslt=rslt[::-1]
    return rslt        
