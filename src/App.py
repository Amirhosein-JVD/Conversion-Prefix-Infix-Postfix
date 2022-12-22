from src.Algorithms.InfixToPostfix import infixToPostfix
from src.Algorithms.InfixToPrefix import infixToPrefix
from src.Algorithms.PostfixToPrefix import postfixToPrefix
from src.Algorithms.PostfixToinfix import postfixToInfix
from src.Algorithms.PrefixToInfix import prefixToInfix
from src.Algorithms.PrefixToPostfix import prefixToPostfix
from src.Algorithms.utility.Functions import isInfix, isPostfix, isPrefix
from src.Algorithms.utility.Tree import drawtree

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
