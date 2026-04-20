class Solution:
    def romanToInt(self, s: str) -> int:
        tr = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

        sm = 0
        prev = 0 
        for l in s:
            # print(l)
            n = tr[l]
            if n <= prev:
                sm += n
            else:
                sm += n - 2*prev

            prev = n
        return sm