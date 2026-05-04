from heapq import heapify, heappop, heappush

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_t = max(grid[0][0], grid[n-1][n-1])

        # this could be done by BFS using a min-heap
        # track max value encountered up to now.
        # the max path_number is the minimum time required

        def adj(i, j):
            child = []
            if i > 0:
                child.append((i-1, j))
            if j > 0:
                child.append((i, j-1))
            if i < n-1:
                child.append((i+1, j))
            if j < n-1:
                child.append((i, j+1))

            return child


        heap = [(grid[0][0], 0, 0)] # val, i, j 
        heapify(heap)
        visited = set()

        res = []

        while heap:
            v, i, j = heappop(heap)

            if (i, j) == (n-1, n-1):
                res.append(v)

            children = adj(i, j)

            for c in children:
                if c not in visited:
                    visited.add(c)
                    u = grid[c[0]][c[1]]
                    heappush(heap, (max(u, v), c[0], c[1]))
        
        return min(res)