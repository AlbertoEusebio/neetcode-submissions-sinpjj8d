class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                l = 0
                while (num + l) in num_set:
                    l+=1
                if l > max_len:
                    max_len = l
        return max_len