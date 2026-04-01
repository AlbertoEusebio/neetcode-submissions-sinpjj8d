
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            m = heapq.heappop(self.nums)
            print(m)

    def add(self, val: int) -> int:
        
        print(self.nums, len(self.nums))

        if len(self.nums) < self.k:
            larg = val
        else:
            m = heapq.heappop(self.nums)
            if m > val:
                larg = m
            else:
                larg = val
        
        heapq.heappush(self.nums, larg)

        return self.nums[0]
