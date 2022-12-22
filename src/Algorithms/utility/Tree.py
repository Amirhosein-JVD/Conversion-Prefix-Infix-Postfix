# We change the drawtree library to run this code

from drawtree import draw_level_order

from Functions import *


def drawtree(infix):
    b = levelOrderList(infix)

    nodes = "["

    for i in b:

        if i != ")" and i != "(":
            nodes += i + ","

    nodes = nodes[:len(nodes) - 1] + "]"

    draw_level_order(nodes)