class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        board = grid

        def dfs(i, j, comp, visited):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            elif int(grid[i][j]) == 0:
                return
            elif visited[i][j] == 1:
                return

            visited[i][j] = 1

            if int(grid[i][j]) != comp:
                grid[i][j] = str(comp)
            
            dfs(i+1, j, comp, visited)
            dfs(i-1, j, comp, visited)
            dfs(i, j+1, comp, visited)
            dfs(i, j-1, comp, visited)

        visited = []

        for i in range(len(board)):
            row = []
            for j in range(len(board[0])):
                row.append(0)
            visited.append(row)
        
        comp = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if int(grid[i][j]) and not visited[i][j]:
                    dfs(i, j, comp, visited)
                    for k in range(len(board)):
                        print(visited[k])

                    for k in range(len(board)):
                        print(board[k])

                    comp += 1

        return comp -1