class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n, m = len(grid), len(grid[0])

        def connect(i, j, val, grid):

            if i < 0 or i >= n or j < 0 or j >= m:
                return
            
            if grid[i][j] != '1':
                return
            
            grid[i][j] = str(val)

            connect(i+1, j, val, grid)
            connect(i-1, j, val, grid)
            connect(i, j+1, val, grid)
            connect(i, j-1, val, grid)



        val = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    connect(i, j, val, grid)
                    val += 1

        # for g in grid:
        #     print(g)

        
        return val-2