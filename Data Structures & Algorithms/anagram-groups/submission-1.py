class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def expnd(s):
            v = {}
            for l in str:
                if l not in v:
                    v[l] = 1
                else:
                    v[l] += 1

            return v

        anagrams = {}

        for st in strs:
            sort = str(sorted(st))
            if sort in anagrams:
                anagrams[sort].append(st)
            else:
                anagrams[sort] = [st]
        
        ret = []
        for l, v in anagrams.items():
            ret.append(v)

        return ret
