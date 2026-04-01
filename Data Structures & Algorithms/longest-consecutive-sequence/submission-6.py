class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1 
        nums = sorted(nums)
        print(nums)

        max_len = 0
        seq_len = 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1] + 1:
                seq_len += 1
            elif nums[i] == nums[i-1]:
                seq_len = seq_len
            else:
                seq_len = 1
            
            if seq_len > max_len:
                max_len = seq_len
        return max_len