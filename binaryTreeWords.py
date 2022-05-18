import os
import string

from Node import Node
from BinaryTree import BinaryTree



def insertFromFile(tree: BinaryTree):
    while True:
        print("\nYou can input path based files, but path must start from the working directory.")
        print(f"Working Directory: {os.getcwd()}")
        print("Input example: ../../example.txt")
        print("Files must be \".txt\"")
        print("All characters will be transformed to lowercase.")
        filename = input("\nFilename # ")

        if len(filename) == 0:
            return
        
        if not filename.endswith(".txt"):
            print(f"\n\n\n\n\nWARNING - Ignoring non .txt file, given filename: {filename}")
            continue
        
        try:
            with open(filename, "r") as f:
                for l in f.readlines():
                    for p in l.split(" "):
                        p = p.lower().strip()
                        if len(p) > 0:
                            tree.insertWord(p)
            
            return
        except FileNotFoundError as e:
            print(f"\n\n\n\n\nWARNING - No file found, given filename: {filename}")



def insertFromInput(tree: BinaryTree):
    while True:
        print("\nInput words to add to BST. (all characters will be transformed to lowercase)")
        phrase = input("\nText # ").strip().lower()
        
        if len(phrase) == 0:
            return
        
        table = str.maketrans(dict.fromkeys(string.punctuation))
        phrase = phrase.translate(table)
        
        for w in phrase.split(" "):
            tree.insertWord(w)
        
        print("\nText inserted with success.\n\n")




def searchWord(tree: BinaryTree):
    while True:
        print("\nWhat is the word you are searching for?")
        word = input("Word # ").lower()
        
        if len(word) == 0:
            return
        
        node = tree.getNodeOfWord(word)
        if node is None:
            print(f"\n\n\n\"{word}\" does not exist on BST.")
        else:
            print(f"\n\n\n\"{word}\" found! {node}")



def searchStartWith(tree: BinaryTree):
    while True:
        print("\nWhat is the term are searching for?")
        word = input("Word # ").lower()
        
        if len(word) == 0:
            return
        
        nodesFound = tree.getNodesStartWith(word)
        if len(nodesFound) == 0:
            print(f"\n\n\nFound 0 words that start with \"{word}\".")
        else:
            print("\n\n")
            for w in nodesFound:
                print(w)
            print(f"Found {len(nodesFound)} words that start with \"{word}\".")





if __name__ == "__main__":
    tree = BinaryTree()

    while True:
        print("\n" * 5)
        print("Word BST menu (lowercase version)")
        print("1 - Insert words from file;")
        print("2 - Insert words from input;")
        print("3 - Find word from input;")
        print("4 - Find words that start with input;")
        print("5 - Balance BST (magical algorithm);")
        print("6 - Balance BST (DSW - Day Stout Warren);")
        print("7 - Print BST;")
        print("8 - Create file of BST;")
        print("0 - Exit;")
        op = -1
        try:
            op = int(input("\nOption # "))
        except ValueError as e:
            continue

        if op == 0:
            exit()

        print("\n" * 10)

        if op == 1:
            insertFromFile(tree)
        elif op == 2:
            insertFromInput(tree)
        elif op == 3:
            searchWord(tree)
        elif op == 4:
            searchStartWith(tree)
        elif op == 7:
            tree.printTree()
        elif op == 8:
            tree.writeFile()