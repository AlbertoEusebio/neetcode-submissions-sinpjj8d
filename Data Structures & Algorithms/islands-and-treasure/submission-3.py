from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # BFS --> start from every treasure cest and ADD the neighbour cells
        # then update the cell IFF the distance from the neighbour is less than current
        # "concurrency" not a problem becuase always minimum

        que = deque([]) # frontier

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    que.append((i,j,0))

        while que:
            i, j, dist = que.popleft()

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                continue
            elif grid[i][j] == -1:
                continue
            elif grid[i][j] < dist:
                continue

            grid[i][j] = dist

            que.append((i+1, j, dist+1))
            que.append((i-1, j, dist+1))
            que.append((i, j+1, dist+1))
            que.append((i, j-1, dist+1))
