class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])


        p=0
        for i in range(n):
            
            for j in range(m):
                if grid[i][j] ==0:
                    continue
                if i-1 < 0:
                    p+=1
                else:
                    p+= 1-grid[i-1][j]
                if i+1>=n:
                    p+=1
                else:
                    p+= 1-grid[i+1][j]
                if j-1<0:
                    p+=1
                else:
                    p+= 1-grid[i][j-1]
                if j+1>=m:
                    p+=1
                else:
                    p+= 1-grid[i][j+1]
        return p