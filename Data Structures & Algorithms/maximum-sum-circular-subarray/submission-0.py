class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        max_sum = max(nums)
        for i in range(len(nums)):
            s = 0
            for j in range(len(nums)):
                s += nums[(i + j) % len(nums)]
                if s > max_sum:
                    max_sum = s
        return max_sum
            