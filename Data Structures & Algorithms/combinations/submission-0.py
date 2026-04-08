class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        comb = []
        
        def dfs(i, res):
            nonlocal comb
            # print(res)
            
            if len(res) == k:
                comb.append(res.copy())
                return

            if i == n+1:
                return

            # take or skip
            dfs(i+1, res.copy())
            dfs(i+1, res + [i])
        
        dfs(1, [])
        return comb
            