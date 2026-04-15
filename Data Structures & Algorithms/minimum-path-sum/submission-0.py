class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Dijkstra

        m, n = len(grid), len(grid[0])

        def children(state):
            i, j = state
            nodes = []

            if i < m-1:
                nodes.append((i+1, j))
            if j < n-1:
                nodes.append((i, j+1))
            return nodes


        v = grid[0][0]
        heap = [(v,0,0)]
        heapq.heapify(heap)
        visited = set()
        #print(visited, heap)

        while heap:

            s, i, j = heapq.heappop(heap)
            #print(s, i, j)
            if (i, j) in visited:
                continue
            if (i, j) == (m-1, n-1):
                return s
            nodes = children((i, j))
            #print(s, i, j, nodes, visited)
            visited.add((i, j))
            for k in nodes:
                a,b = k

                if k not in visited:
                    #visited.add(n)
                    #print(visited)
                    v = s+ grid[a][b]
                    heapq.heappush(heap, (v, a, b))
        return 0