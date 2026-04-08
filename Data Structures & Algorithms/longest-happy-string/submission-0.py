import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = {'a':a, 'b':b, 'c':c}
        used = {'a':0, 'b':0, 'c':0}

        heap = []
        cooldown = []
        heapq.heapify(heap)

        for c,v in freq.items():
            if v == 0:
                continue
            heapq.heappush(heap, (-v, c))

        res = ""
        while heap:

            v, c = heapq.heappop(heap)
            v = -v

            for el in cooldown:
                heapq.heappush(heap, el)
            cooldown = []

            # can not use, cooldown
            if used[c] == 2:
                cooldown.append((-v, c))
                continue  
            elif used[c] == 0:
                used = {'a':0, 'b':0, 'c':0}

            used[c] += 1
            
            res += c
            v -= 1

            if v > 0:
                heapq.heappush(heap, (-v, c))
        
        return res