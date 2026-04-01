class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0:0, 1:0, 2:0}

        for n in nums:
            freq[n] += 1
            
        k = 0
        i = 0
        while i < len(nums):
            while freq[k] == 0:
                k+=1
            
            nums[i] = k
            freq[k] -= 1

            i += 1
