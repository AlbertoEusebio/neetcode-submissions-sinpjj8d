class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board), len(board[0])
        def dfs(i, j, k, visited):

            if k >= len(word):
                return True
            
            if i>= n or i <0 or j>=m or j<0:
                return False

            if visited[i][j]:
                return False

            if board[i][j] != word[k]:
                return False

            visited[i][j]=1


            if dfs(i+1,j, k+1, visited) or dfs(i-1,j, k+1, visited) or dfs(i,j+1, k+1, visited) or dfs(i,j-1, k+1, visited):
                return True

            visited[i][j]=0
            return False
        
        
        visited = []

        for i in range(n):
            visited.append([0]*m)
        for i in range(n):
            for j in range(m):
                #visited[i][j]=1
                if board[i][j] != word[0]:
                    continue
                if dfs(i, j, 0, visited):
                    return True

                #visited[i][j]=0

        return False