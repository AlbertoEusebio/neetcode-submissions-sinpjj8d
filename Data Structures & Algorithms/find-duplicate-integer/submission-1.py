class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        pos = [0] * max(nums)
        for n in nums:
            if pos[n-1] > 0:
                return n
            pos[n-1] +=1