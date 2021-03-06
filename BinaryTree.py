import time

from io import TextIOWrapper
from Node import Node

class BinaryTree:
    def __init__(self, root: Node = None) -> None:
        self.root = root
        self.totalNodes = self.getTotalNodes(node=self.root) if root else 0



    def getTotalNodes(self, node: Node) -> int:
        if node is None:
            return 0

        return 1 + self.getTotalNodes(node.left) + self.getTotalNodes(node.right)



    def getMax(self, node: Node = None) -> Node:
        current = self.root if node is None else node

        while current.right:
            current = current.right
        
        return current



    def getMin(self, node: Node = None) -> Node:
        current = self.root if node is None else node

        while current.left:
            current = current.left
        
        return current



    def insertWord(self, word: str) -> None:
        if self.root is None:
            self.root = Node(word)
            self.totalNodes += 1
            return

        self.__insertWord(self.root, word)



    def __insertWord(self, node: Node, word: str, parent: Node = None) -> Node:
        if node is None:
            self.totalNodes += 1
            newNode = Node(word)
            newNode.parent = parent
            return newNode
        
        if word == node.word:
            node.hit()
            pass
        elif word > node.word:
            node.right = self.__insertWord(node.right, word, node)
        else: 
            node.left = self.__insertWord(node.left, word, node)

        return node



    def remove(self, word: str) -> None:
        self.__remove(self.root, word)



    def __remove(self, node: Node, word: str) -> Node:
        if node is None:
            return None

        if word < node.word:
            node.left = self.__remove(node.left, word)
        elif word > node.word:
            node.right = self.__remove(node.right, word)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.getMin(node.right)

            node.word = temp.word
    
            node.right = self.__remove(node.right, temp.word)

        return node



    def getNodeOfWord(self, word: str, node: Node = None) -> Node:
        if node is None:
            node = self.root
        
        return self.__searchWord(node, word)



    def hasWord(self, word: str, node: Node = None) -> bool:
        if node is None:
            node = self.root
        
        return self.__searchWord(node, word) is not None



    def __searchWord(self, node: Node, word: str) -> Node:
        if node is None:
            return

        if word == node.word:
            return node

        if word > node.word:
            return self.__searchWord(node.right, word)

        return self.__searchWord(node.left, word)



    def getNodesStartWith(self, term: str, node: Node = None) -> list:
        if node is None:
            node = self.root
        
        nodesFound = []
        self.__searchStartWith(node, term, nodesFound)
        return nodesFound



    def __searchStartWith(self, node: Node, term: str, nodesFound: list) -> Node:
        if node is None:
            return

        if node.word.startswith(term):
            nodesFound.append(node)
            self.__searchStartWith(node.right, term, nodesFound)
            self.__searchStartWith(node.left, term, nodesFound)
        else:
            if term > node.word:
                self.__searchStartWith(node.right, term, nodesFound)
            else:
                self.__searchStartWith(node.left, term, nodesFound)
    


    def printTree(self, node: Node = None) -> None:
        if node is None:
            node = self.root

        self.__printTree(node)



    def __printTree(self, node: Node, level: int = 0) -> None:
        if node is not None:
            self.__printTree(node.right, level + 1)
            print(f"{ ' ' * 4 * level }-> { node.word } | { node.total }")
            self.__printTree(node.left, level + 1)



    def printNodeOrder(self, node: Node = None) -> None:
        if node is None:
            node = self.root

        self.__printNodeOrder(self.root)



    def __printNodeOrder(self, node: Node) -> None:
        if node is not None:
            self.__printNodeOrder(node.left)
            print(node.word)
            self.__printNodeOrder(node.right)



    def writeFile(self, node: Node = None, filename: str = None) -> None:
        if node is None:
            if self.root is None:
                print("WARNING: Binary tree root is None, cannot write file of root None")
                return
            
            node = self.root

        if not isinstance(filename, str) or len(filename) == 0:
            filename = time.strftime("%Y%m%d_%H%M%S.txt")
            
        if not filename.endswith(".txt"):
            filename += ".txt"
            
        file = open(filename, "w")
        self.__writeFile(file, node)
        file.close()



    def __writeFile(self, file: TextIOWrapper, node: Node, level: int = 0) -> None:
        if node is not None:
            self.__writeFile(file, node.right, level + 1)
            file.write(f"{ ' ' * 4 * level }-> { node.word } | { node.total }\n")
            self.__writeFile(file, node.left, level + 1)