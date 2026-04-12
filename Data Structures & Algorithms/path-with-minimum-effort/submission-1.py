from collections import deque
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # rows x columns
        rows, cols = len(heights), len(heights[0])
        # bfs with min-heap

        def children(state):

            i, j = state

            nodes = []
            if i > 0:
                nodes.append((i-1, j))
            if i < rows-1:
                nodes.append((i+1, j))
            if j > 0:
                nodes.append((i, j-1))
            if j < cols-1:
                nodes.append((i, j+1))

            return nodes

        que = [(0, (0,0), 0)]
        heapq.heapify(que) # state, effort to get there
        visited = []

        while que:
            # print(que, visited)
            m_dh, state, h = heapq.heappop(que)
            nodes = children(state)
            if state in visited:
                continue

            visited.append(state)

            # print(state, nodes, h, m_dh)
            if state == (rows-1, cols-1):
                print("Fond: ", state, h, m_dh)
                return m_dh

            for n in nodes:
                if n in visited:
                    continue
                dh = abs(heights[state[0]][state[1]] - heights[n[0]][n[1]])
                n_dh = m_dh
                if dh > n_dh:
                    n_dh = dh
                print(n, n_dh)
                heapq.heappush(que, (n_dh, n, h+dh))
            # print(state, h, m_dh, que)
            
        return 0