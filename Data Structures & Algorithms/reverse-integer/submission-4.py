class Solution:
    def reverse(self, x: int) -> int:
        mask = 15

        if x == 0:
            return 0

        res = 0
        s = x // abs(x)
        x = abs(x)
        while x:
            c = x%10
            x //= 10
            res *= 10
            res += c
            if not (-2**31 <= res <= 2**31 - 1):
                return 0

        res *= s

        if -2**31 <= res <= 2**31 - 1:
            return res
        
        return 0