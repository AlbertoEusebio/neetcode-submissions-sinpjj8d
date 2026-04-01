class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for l in s:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1

        for l in t:
            if l not in letters:
                return False
            if letters[l] == 0:
                return False  
            letters[l] -= 1

        for l,v in letters.items():
            if v != 0:
                return False

        return True