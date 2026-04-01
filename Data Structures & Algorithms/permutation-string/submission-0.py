class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_p = {}

        for c in s1:
            s1_p[c] = s1_p.get(c, 0) + 1
        
        i = 0
        while i<len(s2):
            c = s2[i]
            if c in s1_p:
                tmp = s1_p.copy()
                j = i
                while j < len(s2):
                    k = s2[j]
                    if k not in tmp or tmp[k] <= 0:
                        break

                    tmp[k] -= 1
                    j += 1

                print(tmp)
                if sum([v for v in tmp.values()]) == 0:
                    return True
            i += 1

        return False