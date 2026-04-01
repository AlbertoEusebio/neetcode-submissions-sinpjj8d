import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        count = 0
        b = 1
        for i in range(1, n+1):
            a = i
            c = 0
            while a != 0:
                c += a & 1
                a = a >> 1
            res.append(c)

        return res