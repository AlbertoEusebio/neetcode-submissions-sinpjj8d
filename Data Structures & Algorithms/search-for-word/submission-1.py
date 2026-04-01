class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = []
        for r in range(len(board)):
            row = []
            for c in range(len(board[0])):
                row.append(0)
            visited.append(row)

        def dfs(i, j, word, visited):
            print(i, j, word)
            if len(word) == 0:
                return True
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False

            if visited[i][j]:
                return False

            if word[0] != board[i][j]:
                return False

            visited[i][j] = 1

            word = word[1:]
            # print(word, i, j, visited)

            if dfs(i+1, j, word, visited) or dfs(i-1, j, word, visited) or dfs(i, j+1, word, visited) or dfs(i, j-1, word, visited):
                return True
            
            visited[i][j] = 0
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word, visited):
                        return True

        return False