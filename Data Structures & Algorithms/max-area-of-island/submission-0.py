class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j, comp, visited):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            elif grid[i][j] == 0:
                return 0
            elif visited[i][j] == 1:
                return 0

            visited[i][j] = 1

            if grid[i][j] != comp:
                grid[i][j] = comp

            a = dfs(i+1, j, comp, visited)
            b = dfs(i-1, j, comp, visited)
            c = dfs(i, j+1, comp, visited)
            d = dfs(i, j-1, comp, visited)

            return a + b + c + d + 1

        visited = []
        for i in range(len(grid)):
            visited.append([0] * len(grid[0]))

        comp = 1
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not visited[i][j]:
                    area = dfs(i, j, comp, visited)
                    
                    if area > max_area:
                        max_area = area
                    
                    comp += 1

        for i in range(len(grid)):
            print(visited[i])
        print()
        for i in range(len(grid)):
            print(grid[i])
        return max_area