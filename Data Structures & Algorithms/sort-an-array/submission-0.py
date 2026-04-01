import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        h = []
        heapq.heapify(h)

        while len(nums):
            n = nums.pop()
            heapq.heappush(h, n)

        while h:
            n = heapq.heappop(h)
            nums.append(n)
        return nums