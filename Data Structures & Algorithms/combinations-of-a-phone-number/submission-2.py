class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lett = "ABCDEFGHIJKLMNOQRSTUVXYZ"
        m = {}

        for i in range(2,10):
            m[i] = lett[(i-2)*3:(i-2)*3+3]

        m[7] += 'P'
        m[9] += 'W'

        print(m)
        res = []
        def dfs(pref, dig):
            if len(dig) < 1:
                return
            if len(dig) == 1:
                ld = m[int(dig[0])].lower()
                for l in ld:
                    res.append(pref + l)
                return
        
            ld = m[int(dig[0])].lower()
            for l in ld:
                pref_n = pref + l
                dfs(pref_n, dig[1:])


        dfs("", digits)

        return res