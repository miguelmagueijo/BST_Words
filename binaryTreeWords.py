from Node import Node
from BinaryTree import BinaryTree



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