from utility.Functions import*

def infixToPrefix(exp):

    exp = exp[::-1]

    operators = []

    result = ''

    for i in exp:

        if(isOperator(i)):

            if((len(operators)>0) and (operators[-1]!=')')):

                if(Precedence(i)>Precedence(operators[-1])):

                    operators.append(i)
                
                else:

                    if(i=='^' and operators[-1]=='^'):

                        result+=operators[-1]

                        operators.pop()

                        operators.append(i)
                    
                    else:

                        while(len(operators)!=0 and Precedence(i)<Precedence(operators[-1])):

                            result+=operators[-1]

                            operators.pop()

                        operators.append(i)
        
            else:

                operators.append(i)
        
        elif(i==')'):

            operators.append(i)

        elif(i=='('):

            k=''

            while(k!=')'):

                k=operators[-1]

                if(k!=')'):

                    result+=k

                operators.pop()

        else:

            result+=i

    while(len(operators)!=0):

        result+=operators[-1]

        operators.pop()

    result = result[::-1]

    return result
