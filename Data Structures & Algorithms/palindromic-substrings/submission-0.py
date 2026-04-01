class Solution:
    def countSubstrings(self, s: str) -> int:
        
        pal = {}

        def is_pal(st):
            if st in pal:
                pal[st] += 1
                return True

            if st == st[::-1]:
                pal[st] = 1
                return True
            return False

        if len(s) == 1:
            return 1
        
        for l in range(len(s), 0, -1):
            for i in range(0, len(s)-l+1):
                is_pal(s[i:i+l])

        return sum(pal.values())
