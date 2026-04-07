class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        v = 0

        for n in nums:
            v |= n
        
        return v << len(nums) -1 