class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = 0
        for c in a:
            if c == '1':
                # print(c)
                na = na | 1
            na = na << 1
        na = na >> 1

        nb = 0
        for c in b:
            if c == '1':
                # print(c)
                nb = nb | 1
            nb = nb << 1
        nb = nb >> 1
        
        nc = na + nb

        if nc == 0:
            return '0'

        res = ''
        while nc > 0:
            c = chr((nc & 1) + ord('0'))
            # print(c)
            nc = nc >> 1
            res += c
        
        return res[::-1]