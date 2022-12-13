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

    myLen=len(infixExp)
    counter=0
    max=0
    for i in infixExp:
        if(i=='('):counter+=1
        elif(i==')'):counter-=1
        if(counter>max):max=counter
    myList=[]
    for i in range(max):
        temp=[]
        myList.append(temp)
    resLen=((2**(max+1))-1)
    res=[None]*resLen
    for i in range(myLen):
        myChar=infixExp[i]
        if(myChar=='('):counter+=1
        elif(myChar==')'):counter-=1
        elif(isOperator(infixExp[i])):
            temp=[infixExp[i],infixExp[i-1]+infixExp[i+1]]
            myList[counter-1].append(temp)

    
    for i in range(max):
        iListLength=len(myList[i])
        for j in range(2**i):
            if(j<iListLength):

                min=0
                for k in range(min,resLen):
                    if(res[k]==None):
                        res[k]=myList[i][j][0]
                        min+=1
                        break

                if(myList[i][j][1][0]!=')'):
                    myIndex=(((2**(i+1))-1)+2*(j+1)-2)
                    if(res[myIndex]==None):
                        res[myIndex]=myList[i][j][1][0]
                    else:
                        for k in range(myIndex+1,resLen):
                            if(res[k]==None):
                                res[k]=myList[i][j][1][0]
                                break
                    for p1 in range(max-1):
                        myIndex2=(((2**(i+2+p1))-1)+(j*(2**(p1+2))))
                        end=myIndex2+2**(p1+1)
                        if(end<=resLen):
                            for p in range(myIndex2,end):
                                if(res[p]==None):
                                    res[p]='#'
                        else:break

                if(myList[i][j][1][1]!='('):

                    myIndex=(((2**(i+1))-1)+2*(j+1)-1)

                    if(res[myIndex]==None):
                        res[myIndex]=myList[i][j][1][1]
                    else:
                        for k in range(myIndex+1,resLen):
                            if(res[k]==None):
                                if(myList[i][j][1][0]==')'):
                                    res[k+1]=myList[i][j][1][1]
                                    break
                                elif(myList[i][j][1][0]!=')'):
                                    res[k]=myList[i][j][1][1]
                                    break

                    for p1 in range(max-1):
                            myIndex2=(((2**(i+2+p1)-1)+(j+1)*(2**(p1+2))))         
                            if(myIndex2<=resLen):
                                start=myIndex2-(2**(p1+1))
                                for p in range(start,myIndex2):
                                    if(res[p]==None):
                                        res[p]='#'
                            else:break
            else:
                break

    if(None in res):
        for i in range(resLen):
            if(res[i]==None):res[i]='#'

    return res


