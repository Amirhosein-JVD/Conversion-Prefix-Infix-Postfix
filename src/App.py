from Functions import *
from InfixToPrefix import *
from InfixToPostfix import *
from PrefixToPostfix import *
from PrefixToInfix import *
from PostfixToinfix import *
from PostfixToPrefix import *
from Tree import *

expression = input()

if isInfix(expression):

    print("Prefix : " + str(infixToPrefix(expression)))
    print("Postfix : " + str(infixToPostfix(expression)))
    drawtree(expression)

elif isPostfix(expression):

    print("Infix : " + str(postfixToInfix(expression)))
    print("Prefix : " + str(postfixToPrefix(expression)))
    drawtree(postfixToInfix(expression))

elif isPrefix(expression):

    print("Infix : " + str(prefixToInfix(expression)))
    print("Postfix : " + str(prefixToPostfix(expression)))
    drawtree(prefixToInfix(expression))
