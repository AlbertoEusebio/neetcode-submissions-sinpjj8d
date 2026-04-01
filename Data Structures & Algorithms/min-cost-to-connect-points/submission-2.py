import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Union find
        # Where parents are connected components
        # Form all possible edges

        edges = []
        heapq.heapify(edges)

        for p in range(len(points)):
            for q in range(p+1, len(points)):
                if p == q:
                    continue
                d = abs(points[p][0] - points[q][0]) + abs(points[p][1] - points[q][1])
                heapq.heappush(edges, [d, p, q])

        # Now that we have all edges, we can push it to a min-heap
        # then we pop from min-heap till all points connected

        parents = [i for i in range(len(points))]
        ranks = [1] * len(points)

        # print(edges)

        total = 0
        while edges:
            d, p, q = heapq.heappop(edges)

            if parents[p] == parents[q]:
                # skip edge
                continue

            total += d
            g= parents[q]
            m = parents[p]
  
            if ranks[p] >= ranks[q]:
                ranks[p] += ranks[q]
                for k in range(len(parents)):
                    if parents[k] == g:
                        parents[k] = m
            else:
                ranks[q] += ranks[p]
                for k in range(len(parents)):
                    if parents[k] == m:
                        parents[k] = g

            print(d, p, q, parents)


        return total