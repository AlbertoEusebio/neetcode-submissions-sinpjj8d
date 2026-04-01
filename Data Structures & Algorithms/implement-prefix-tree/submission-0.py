class Node:
    def __init__(self, c):
        self.c = c
        self.is_word_end = False
        self.leaves = {}

class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        tree = self.tree
        for c in word:
            if c not in tree.keys():
                print('insert', c)
                tree[c] = Node(c)
            n = tree[c]
            tree = tree[c].leaves

        n.is_word_end = True

    def search(self, word: str) -> bool:
        tree = self.tree
        for c in word:
            print(c)
            if c not in tree.keys():
                return False
            n = tree[c]
            tree = tree[c].leaves

        if not n.is_word_end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        tree = self.tree
        for c in prefix:
            print(c)
            if c not in tree.keys():
                return False
            tree = tree[c].leaves
        
        return True