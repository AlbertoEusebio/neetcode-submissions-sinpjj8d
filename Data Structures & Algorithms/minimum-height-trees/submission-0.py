import heapq

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for e in edges:
            a, b = e
            graph[a].append(b)
            graph[b].append(a)
        
        heap = []
        heapq.heapify(heap)

        print(graph)

        for i in range(n):
            h_max = 0
            que = deque([(i, h_max)])
            visited = set([i])

            while que:
                n, h = que.popleft()

                children = graph[n]
                if h > h_max:
                    h_max = h

                for c in children:
                    if c not in visited:
                        visited.add(c)
                        que.append((c, h+1))
            
            heapq.heappush(heap, (h_max, i))
        
        print(heap)

        h_min = heap[0][0]
        res = []

        while heap:
            h, i = heapq.heappop(heap)
            if h > h_min:
                return res
            res.append(i)
        return res