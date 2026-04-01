class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # The Os in the border can 'clear' some regions, all the rest remains uncleared

        def dfs(i, j, visited):

            # Are we still in the graph
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            
            if visited[i][j]:
                return
            
            if board[i][j] == 'X':
                return
            
            visited[i][j] = 1

            dfs(i+1, j, visited)
            dfs(i-1, j, visited)
            dfs(i, j+1, visited)
            dfs(i, j-1, visited)

        visited = []
        for i in range(len(board)):
            visited.append([0] * len(board[0]))

        for i in range(len(board)):
            dfs(i, 0, visited)
            dfs(i, len(board[0])-1, visited)

        for j in range(len(board[0])):
            dfs(0, j, visited)
            dfs(len(board)-1, j, visited)

        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'

        
