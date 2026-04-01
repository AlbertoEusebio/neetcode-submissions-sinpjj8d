class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        visited =[[0]*n for _ in range(m)]


        res = 0
        def dfs(p):
            nonlocal res
            i, j =p

            if i>= m or j>=n:
                return
            if visited[i][j]:
                return
            if i==m-1 and j == n-1:
                res+=1
                return

            visited[i][j] =1
            
            # down 
            dfs((i+1, j))
            dfs((i, j+1))
            visited[i][j] =0

        dfs((0,0))
        return res