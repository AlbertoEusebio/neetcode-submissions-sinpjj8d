class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        res = []

        def dfs(i, comb):

            if i >= len(candidates):
                return

            # [0] --> add 0 index element
            comb.append(candidates[i])
            # print(comb)

            if sum(comb) == target:
                res.append(comb.copy())
            elif sum(comb) > target:
                # comb.pop() # current element is too much
                # dfs(i+1, comb) 
                return
                      
            # less than target
            dfs(i+1, comb.copy()) # always next because can not add already selected
            comb.pop()
            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]: 
                j+= 1 
            dfs(j, comb.copy())


        dfs(0, [])

        return res