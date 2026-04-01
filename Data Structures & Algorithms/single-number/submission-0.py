class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dict is 0(n) space
        # array too --> but we can use a number

        a = 0 # big number

        for n in nums:
            a = a ^ n
    
        return a