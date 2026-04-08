import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        cooldown = []
        heap = []
        heapq.heapify(heap)

        freq = defaultdict(int)

        for c in s:
            freq[c] += 1

        for c,v in freq.items():
            heapq.heappush(heap, (-v, c))

        print(heap)
        
        res = ""
        i = 0
        while heap: 
            # print(i, heap, cooldown)

            v, c = heapq.heappop(heap)
            v = -v
            res += c
            v -= 1
            # print(i, v, c)
            # empty cooldown - 1 element always ideally
            for el in cooldown:
                heapq.heappush(heap, el)
            cooldown = []

            if v > 0:
                # put it back
                cooldown.append((-v, c))

            # print(i,heap, cooldown)
            # i+=1


        if len(cooldown) > 0:
            for el in cooldown:
                heapq.heappush(heap, el)

            if heap[0][1] == res[-1]:
                return ""
            else:
                print(heapq)
                return None
        return res
