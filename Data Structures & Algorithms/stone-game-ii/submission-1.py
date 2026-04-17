class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        dp = {}

        def dfs(i, turn, M):
            # X --> M
            if i == len(piles):
                return 0

            if (i, turn, M) in dp:
                return dp[(i, turn, M)]

            res = 0 if turn==1 else float('inf')
            s = 0
            for x in range(1, 2*M+1):

                if i+x > len(piles):
                    break

                s += piles[i + x -1]

                # print(turn, i, x, stones + s)
                rc = dfs(i+x, turn * (-1), max(M, x))
                
                if turn == 1:
                    res = max(res, rc + s)
                else:
                    res = min(res, rc)

                # print(i, x, res)

            dp[(i, turn, M)] = res

            return res

        return dfs(0, 1, 1)