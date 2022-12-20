from drawtree import draw_level_order

from src.InfixToPrefix import infixToPrefix

from Functions import *

a = input("Please Enter Your Expression: ")

b = levelOrderList(a)

nodes = "["

for i in b:

    if i != ")" and i != "(":

        nodes += i + ","

nodes = nodes[:len(nodes) - 1] + "]"

draw_level_order(nodes)