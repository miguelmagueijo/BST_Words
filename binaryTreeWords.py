from io import TextIOWrapper
import time


class Node:
    def __init__(self, word: str, parent = None, left = None, right = None ) -> None:
        if not isinstance(word, str):
            raise ValueError("Node value must be a string")
        
        self.word = word
        self.left = left
        self.right = right
        self.parent = parent
        self.total = 1 # count the times user tried to insert the same word

    def hit(self):
        self.total += 1

    def __str__(self) -> str:
        return f"Node -> Word: {self.word} | Total {self.total}"



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



    def __insertWord(self, node: Node, word: str, parent: Node = None):
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



    def remove(self, word: str):
        self.__remove(self.root, word)



    def __remove(self, node: Node, word: str):
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

    def getNodeOfWord(self, word: str, node: Node = None):
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
            nodesFound.append(node.word)
            self.__searchStartWith(node.right, term, nodesFound)
            self.__searchStartWith(node.left, term, nodesFound)
        else:
            if term > node.word:
                self.__searchStartWith(node.right, term, nodesFound)
            else:
                self.__searchStartWith(node.left, term, nodesFound)
    

    
    def printTree(self, node: Node, level: int = 0) -> None:
        if node is not None:
            self.printTree(node.right, level + 1)
            print(f"{ ' ' * 4 * level }-> { node.word } | { node.total }")
            self.printTree(node.left, level + 1)



    def printNodeOrder(self, node: Node) -> None:
        if node is not None:
            self.printNodeOrder(node.left)
            print(node.word)
            self.printNodeOrder(node.right)



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



if __name__ == "__main__":
    # nodeTeste = Node("teste")
    # nodeTeste.left = Node("bacalhau")
    # nodeTeste.right = Node("yogurt")
    # nodeTeste.left.left = Node("ana")
    # nodeTeste.right.left = Node("uvas")
    # nodeTeste.right.right = Node("zebra")
    # ab = BinaryTree(nodeTeste)
    ab = BinaryTree()
    ab.insertWord("teste")
    ab.insertWord("bacalhau")
    ab.insertWord("yogurt")
    ab.insertWord("ana")
    ab.insertWord("uvas")
    ab.insertWord("zebra")
    ab.insertWord("zab")
    ab.insertWord("zzz")
    ab.printTree(ab.root)

    print("\n\n")
    ab.remove("teste")
    ab.printTree(ab.root)
    print(ab.hasWord("ana"))
    print(ab.getNodesStartWith(""))
    exit()
    print(ab.totalNodes)
    ab.printNodeOrder(ab.root)
    ab.printTree(ab.root)
    print(f"Max: { ab.getMax() }")
    print(f"Min: { ab.getMin() }")
    # ab.writeFile()