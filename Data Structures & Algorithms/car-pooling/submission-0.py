import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        heap = []
        heapq.heapify(heap)

        for trp in trips:
            c, s, e = trp
            # push start and end events to the heap
            # start get a 1, ends a 0
            # this way when s, e are equal, ends come before

            heapq.heappush(heap, (s, 1, c)) # add capacity 
            heapq.heappush(heap, (e, 0, c)) #remove capacity
            # if overflows then return False

        cp = 0
        # print(heap)
        while heap:
            v, o, c = heapq.heappop(heap)
            # print(cp, v, c, o)
            if o:
                cp += c
            else:
                cp -= c
            
            if cp > capacity:
                return False
        return True
