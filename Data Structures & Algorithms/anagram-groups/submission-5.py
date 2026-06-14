class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        def vector(s):
            v = [0] * 26
            for c in s:
                i = ord(c) - ord('a') if c.islower() else ord(c) - ord('A')
                v[i] += 1

            return str(v)

        anagrams = {}

        for st in strs:
            v = vector(st)
            if v in anagrams:
                anagrams[v].append(st)
            else:
                anagrams[v] = [st]

        ret = []
        for _, lst in anagrams.items():
            ret.append(lst)

        return ret