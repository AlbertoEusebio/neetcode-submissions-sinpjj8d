class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""

        l = len(min(strs, key= lambda s: len(s)))

        for i in range(l):
            p = strs[0][i]
            for s in strs:
                if s[i] != p:
                    return pref
            pref += p
        return pref