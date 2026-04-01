class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        m = max(1, max(nums)+1)
        
        tab = {}

        for n in nums:
            if n <= 0:
                continue
            tab[n] = 1
        
        i = 1
        while i in tab:
            i += 1

        return i