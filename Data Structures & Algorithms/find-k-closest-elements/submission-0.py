import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist = []
        heapq.heapify(dist)

        for n in arr:
            heapq.heappush(dist, (abs(x-n), n))

        res = []
        for i in range(k):
            _, n = heapq.heappop(dist)
            res.append(n)
        return sorted(res)