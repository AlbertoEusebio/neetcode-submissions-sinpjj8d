class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = sum(nums)

        s = 0
        cs = 0
        max_sum = nums[0]
        min_sum = nums[0]
        for n in nums:
            if s + n > n:
                s += n
            else:
                s = n

            if s > max_sum:
                max_sum = s

            if cs + n < n:
                cs += n
            else:
                cs = n

            if cs < min_sum:
                min_sum = cs

        print(max_sum, min_sum)

        if max_sum <= 0:
            return max_sum
        
        return max(max_sum, total-min_sum)
