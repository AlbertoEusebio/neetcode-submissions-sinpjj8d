

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        costs_precomp = [-1] * (n+2)

        def dfs(i, c):

            if i > n:
                return 2**30
            elif i == n:
                # print(i, c)
                return c
        
            c += cost[i] # current cost
            # print(' '*i, i, c)

            a =  costs_precomp[i+1] if costs_precomp[i+1] != -1 else (dfs(i+1, c) - c) # cost in hindsight
            b =  costs_precomp[i+2] if costs_precomp[i+2] != -1 else (dfs(i+2, c) - c)

            costs_precomp[i] = min(a, b) + cost[i]

            # print(costs_precomp, ' '*i, i, c, a, b, min(a, b) + c)
            print(costs_precomp)

            return min(a, b) + c
        
        return min(dfs(0, 0), dfs(1, 0))