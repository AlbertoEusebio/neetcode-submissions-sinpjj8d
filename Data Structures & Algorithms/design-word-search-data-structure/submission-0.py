class Node:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = Node()
            
            n = tree[c]
            tree = n.children
        n.is_word_end = True

    def search(self, word: str) -> bool:
         
        def dfs(tree, i):

            if i >= len(word):
                return False

            c = word[i]

            if i == len(word) - 1:
                if c == '.':
                    ret = []
                    for char in tree:
                        n = tree[char]
                        ret.append(n.is_word_end)
                    return any(ret)
                elif c in tree:
                    return tree[c].is_word_end
                return False
            
            if c == '.':
                # dfs all directions
                ret = []
                for char in tree:
                    n = tree[char]
                    ret.append(dfs(n.children, i+1))
                return any(ret)

            elif c not in tree:
                return False
            
            n = tree[c]
            tree = n.children
            return dfs(n.children, i+1)
            
        return dfs(self.tree, 0)