class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)

        MAX_INT = max(n,m) + 1

        memo = {}

        def dfs(i, j):
            # print(s, i, word2, j)

            if i == n:
                # print("Yuppy", c)
                return m - j
            elif j == m:
                # print("Nope")
                return n - i

            if (i, j) in memo:
                return memo[(i,j)]

            # equal, go to next
            if word1[i] == word2[j]:
                return dfs(i+1, j+1) # skip

            # drop letter
            b = dfs(i+1, j)

            # insert letter to current
            a = dfs(i, j+1)

            # change letter
            c = dfs(i+1, j+1)

            res = min(a,b,c) + 1

            memo[(i, j)] = res

            return res

        return dfs(0,0)
