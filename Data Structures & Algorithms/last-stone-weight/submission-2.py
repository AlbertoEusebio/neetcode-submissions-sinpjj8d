import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # create max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)

            if x == y:
                continue
            mx = max(x, y)
            mn = min(x, y)

            heapq.heappush(stones, -(mx - mn))

        if len(stones) == 0:
            return 0
        
        return -stones[0]


