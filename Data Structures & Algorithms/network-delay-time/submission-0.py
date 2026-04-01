import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra --> revise

        nodes = {}

        for i in range(n):
            nodes[i] = []

        for time in times:
            i, j, t = time
            nodes[i-1].append((j-1, t))
            # nodes[j-1].append((i-1, t))


        dist = [1001] * n # Distance init to infinity (max possible time)
        priority_queue = []

        # PRiority queue contains the Node and the distance (distance first)
        heapq.heapify(priority_queue) # by default a min_heap --> Perfect because shortest path
        heapq.heappush(priority_queue, (0, k-1))
        dist[k-1] = 0  # updated dist

        while priority_queue:
            d, u = heapq.heappop(priority_queue)
            print(dist, d, u+1)

            for v, t in nodes[u]:
                if dist[v] > dist[u] + t:
                    dist[v] = dist[u] + t
                    heapq.heappush(priority_queue, (dist[u] + t, v))
            
        m = max(dist)

        if m >= 1001:
            return -1
        
        return m