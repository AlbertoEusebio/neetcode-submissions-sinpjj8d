import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums) # min heap

        # keep only k largest
        while len(nums) > k:
            heapq.heappop(nums)

        # k largest elements

        return nums[0]