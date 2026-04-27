class Node:
    def __init__(self, char):
        self.c = char
        self.children = {}
        self.eow = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n,m = len(board), len(board[0])

        trie = Node(None)
        for wrd in words:
            h = trie
            for c in wrd:
                if c in h.children:
                    h = h.children[c]
                else:
                    nd = Node(c)
                    h.children[c] = nd
                    h = nd
            h.eow = True

        
        visited = [[0]*m for _ in range(m)]
        word_found = set()


        def dfs(i, j, h, visited, s):
            nonlocal word_found
            if i < 0 or i >= n or j <0 or j >= m or visited[i][j]:
                return False

            if board[i][j] != h.c:
                return False
            
            if h.eow:
                word_found.add(s)

            visited[i][j] = 1
            for ch in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                a, b = ch
                
                if a < 0 or a >= n or b <0 or b >= m or visited[a][b]:
                    continue
                
                ngb = board[a][b]
                if ngb not in h.children:
                    continue
                
                nd = h.children[ngb]
                dfs(a, b, nd, visited, s + ngb)
                
            visited[i][j] = 0

            return False

        for i in range(n):
            for j in range(m):
                ngb = board[i][j]
                if ngb in trie.children:
                    nd = trie.children[ngb]
                    dfs(i, j, nd, visited, ngb)
        return list(word_found)