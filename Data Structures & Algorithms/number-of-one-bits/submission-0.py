class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # 1 bitmask

        b = 1
        count = 0
        while n:
            count += n & b
            n = n >> 1
        
        return count