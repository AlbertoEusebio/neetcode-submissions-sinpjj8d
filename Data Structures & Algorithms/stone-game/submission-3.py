class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        tot = sum(piles)

        memo = {}

        def dfs(i, j, s, turn):

            if i > j:
                return s > 0

            if (i, turn) in memo:
                return memo[(i, turn)]

            # take beginning or end

            v = piles[i] if turn == 1 else 0
            u = piles[j] if turn == 1 else 0

            res = max(dfs(i+1, j, s+v, -1*turn), dfs(i, j-1, s+u, -1*turn))
            memo[(i,turn)] = res
            return res
        return dfs(0, len(piles)-1, 0, 1)