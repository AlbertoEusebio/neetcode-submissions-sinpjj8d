from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        que = deque()
        t = 0

        # put all rotten fruits in frontier
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i+1, j, t))
                    que.append((i-1, j, t))
                    que.append((i, j+1, t))
                    que.append((i, j-1, t))
        
        while que:
            i, j, t = que.popleft()

            # sanity chech
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                continue
            elif grid[i][j] == 0:
                continue
            elif grid[i][j] == 2:
                continue

            # if grid is 1 --> rotten
            grid[i][j] = 2

            # iterate on adjacent
            que.append((i+1, j, t+1))
            que.append((i-1, j, t+1))
            que.append((i, j+1, t+1))
            que.append((i, j-1, t+1))

        print(grid)
        # if remaining then 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1


        return t