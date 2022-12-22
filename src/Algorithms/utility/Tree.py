from src.Algorithms.utility.Functions import levelOrderList
from src.drawtree.drawtree import draw_level_order


def drawtree(infix):
    b = levelOrderList(infix)

    nodes = "["

    for i in b:

        if i != ")" and i != "(":
            nodes += i + ","

    nodes = nodes[:len(nodes) - 1] + "]"

    draw_level_order(nodes)
