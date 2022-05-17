import os
import time

from Node import Node
from BinaryTree import BinaryTree



def insertFromFile(tree: BinaryTree):
    while True:
        print("\nYou can input path based files, but path must start from the working directory.")
        print(f"Working Directory: {os.getcwd()}")
        print("Input example: ../../example.txt")
        print("Files must be \".txt\"")
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
            continue

        if op == 7:
            tree.printTree()
            continue
        
        if op == 8:
            tree.writeFile()
            continue