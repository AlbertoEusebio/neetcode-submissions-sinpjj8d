class Solution:
    def mySqrt(self, x: int) -> int:
        # x ** 0.5 --> 
        if x <= 1:
            return x

        i,j= 0, x
        m = (i+j) // 2
        while i < j:
            print(m)
            if m*m > x:
                j = m-1
            elif m*m < x:
                i = m+1
            else:
                return m

            m = (i+j) //2
        return m if m*m <= x else m-1
