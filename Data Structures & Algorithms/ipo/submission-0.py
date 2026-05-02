from heapq import heapify, heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        # create a min-heap of sustainable costs
        # create a max-heap of profits

        cst_heap = [(c,i) for i,c in enumerate(capital)]
        prf_heap = []

        heapify(cst_heap)
            
        while cst_heap and cst_heap[0][0] <= w:
            c, j = heappop(cst_heap)
            z = profits[j]
            # print(c, z)
            heappush(prf_heap, (-z))

        print(prf_heap)
        
        i = 0
        while prf_heap and i < k:
            p = -heappop(prf_heap)
            w += p
            i += 1
            while cst_heap and cst_heap[0][0] <= w:
                _, j = heappop(cst_heap)
                z = profits[j]
                heappush(prf_heap, (-z))


        return w
