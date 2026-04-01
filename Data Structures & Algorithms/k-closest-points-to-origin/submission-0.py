import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = [(sqrt((p[0])**2 + (p[1])**2), p) for p in points]

        heapq.heapify(distances)

        closest = []

        print(distances)

        i = 0
        while i < k:
            p = heapq.heappop(distances)
            closest.append(p[1])
            i += 1

        print(closest)


        return closest