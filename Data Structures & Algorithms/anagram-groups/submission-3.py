class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def expnd(s):
            count = [0] * 26
            for l in s:
                i = ord(l) - ord('a') if l.islower() else ord('A')
                count[i] += 1

            return tuple(count)

        anagrams = {}

        for st in strs:
            if expnd(st) not in anagrams:
                anagrams[expnd(st)] = [st]
            else:
                anagrams[expnd(st)].append(st)

        ret = []

        for k,v in anagrams.items():
            ret.append(v)

        return ret
