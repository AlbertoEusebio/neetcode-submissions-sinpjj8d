
class Solution:
    def isHappy(self, n: int) -> bool:
        # 100, 1000, ... 
        # 2 --> 2**x

        seen = [0]* 10

        while n != 1:

            if n < 10 and seen[n] == 1:
                return False
            elif n < 10 and seen[n] == 0:
                seen[n] = 1

            tmp = n
            n = 0

            while tmp:
                n += (tmp%10)**2
                tmp = tmp // 10

        return True
