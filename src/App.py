from Algorithms.InfixToPrefix import *
from Algorithms.InfixToPostfix import *
from Algorithms.PrefixToPostfix import *
from Algorithms.PrefixToInfix import *
from Algorithms.PostfixToinfix import *
from Algorithms.PostfixToPrefix import *
from Algorithms.utility.Tree import *

expression = input("Please Enter Your Expression : ")

if isInfix(expression):

    print()
    print("This expression is infix.")
    print("----------------------------------------------------")
    print("Prefix : " + str(infixToPrefix(expression)))
    print("Postfix : " + str(infixToPostfix(expression)))
    print("----------------------------------------------------")
    print("expression tree : ")
    print()
    drawtree("(" + expression + ")")

elif isPostfix(expression):

    print()
    print("This expression is postfix.")
    print("-----------------------------------------------------")
    print("Infix : " + str(postfixToInfix(expression)))
    print("Prefix : " + str(postfixToPrefix(expression)))
    print("-----------------------------------------------------")
    print("expression tree after postfix to infix conversion : ")
    print()
    drawtree(postfixToInfix(expression))

elif isPrefix(expression):

    print()
    print("This expression is prefix.")
    print("----------------------------------------------------")
    print("Infix : " + str(prefixToInfix(expression)))
    print("Postfix : " + str(prefixToPostfix(expression)))
    print("----------------------------------------------------")
    print("expression tree after prefix to infix conversion : ")
    print()
    drawtree(prefixToInfix(expression))
