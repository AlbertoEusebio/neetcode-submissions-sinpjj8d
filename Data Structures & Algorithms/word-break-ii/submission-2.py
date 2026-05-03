class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []

        def dfs(st, curr):
            nonlocal res
            # print(st, curr)

            if st == '':
                res.append(' '.join(curr))
                return ' '.join(curr)

            for i in range(len(st)+1):
                cst = st[:i]
                if cst in wordDict:
                    dfs(st[i:], curr + [cst])
        
        dfs(s, [])
        return res