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