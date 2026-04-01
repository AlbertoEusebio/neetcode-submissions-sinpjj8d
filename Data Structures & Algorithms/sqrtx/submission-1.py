class Solution:
    def mySqrt(self, x: int) -> int:
        # x ** 0.5 --> 
        if x <= 1:
            return x

        for i in range(x):
            if i*i > x:
                return i-1
        