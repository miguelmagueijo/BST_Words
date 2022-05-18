import math

from BinaryTree import BinaryTree
from Node import Node

# Code based from GfG: https://www.geeksforgeeks.org/day-stout-warren-algorithm-to-balance-given-binary-search-tree/

class DSW:
    def bstToVine(self, grand: Node):
        count = 0
        tmp = grand.right

        while tmp:
            if tmp.left:
                oldTmp = tmp
                tmp = tmp.left
                oldTmp.left = tmp.right
                tmp.right = oldTmp
                grand.right = tmp
            else:
                count += 1
                grand = tmp
                tmp = tmp.right

        return count

    def compress(self, grand: Node, m):
        tmp = grand.right
        i = 0

        while i < m:
            oldTmp = tmp
            tmp = tmp.right
            grand.right = tmp
            oldTmp.right = tmp.left
            tmp.left = oldTmp
            grand = tmp
            tmp = tmp.right
            i += 1

    def balance(self, tree: BinaryTree) -> bool:
        if tree.totalNodes == 0:
            return False
        
        grand = Node("")
        grand.right = tree.root
        count = self.bstToVine(grand)
        h = math.log2(count + 1)
        m = math.pow(2, h) - 1
        self.compress(grand, count - m)
        m = math.floor(m / 2)
        while m > 0:
            self.compress(grand, m)
            m = math.floor(m / 2)

        tree.root = grand.right

        return True