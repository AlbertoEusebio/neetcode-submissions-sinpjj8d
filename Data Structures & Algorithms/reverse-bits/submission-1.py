class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(31):
            
            res |= n & 1
            res = res << 1

            n = n >> 1
        
        res |= n & 1
        print(bin(res))
        
        return res