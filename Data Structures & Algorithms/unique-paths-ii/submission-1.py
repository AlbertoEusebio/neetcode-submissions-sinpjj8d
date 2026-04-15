class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        memo = {}
        visited = [[0] * n for _ in range(m)]

        def dfs(i, j, visited):

            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or obstacleGrid[i][j]:
                return 0

            if (i, j) == (m-1, n-1):
                for v in visited:
                    print(v)
                print()
                return 1

            if (i, j) in memo:
                return memo[(i,j)]

            visited[i][j] = 1
            # all paths
            memo[(i, j)] = dfs(i+1, j, visited) + dfs(i, j+1, visited)
            visited[i][j] = 0
            
            return memo[(i, j)]

        return dfs(0, 0, visited)