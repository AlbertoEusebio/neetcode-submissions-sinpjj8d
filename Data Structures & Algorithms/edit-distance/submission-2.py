class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)

        MAX_INT = max(n,m) + 1

        letters = 'abcdefghijklmnopqrstuvwxyz'

        def dfs(i, j, s, c):
            # print(s, i, word2, j)

            if i>= len(s) and s == word2:
                # print("Yuppy", c)
                return c
            elif i>=len(s) and j>= m:
                # print("Nope")
                return MAX_INT

            if i < len(s) and j>=m:
                # drop
                return dfs(i, j, s[:i] + s[i+1:], c+1)
            elif j<m and i>=len(s):
                # add
                return dfs(i+2, j+1, s[:i+1] + word2[j] + s[i+1:], c+1)

            # equal, go to next
            if s[i] == word2[j]:
                return dfs(i+1, j+1, s, c) # skip

            # drop letter
            b = dfs(i, j, s[:i] + s[i+1:], c+1)


            # change letter to current
            a = dfs(i+1, j+1, s[:i] + word2[j] + s[i+1:], c+1)

            c = dfs(i+1, j+1, s[:i] + word2[j] + s[i:], c+1)

            # insert letter
            # c = MAX_INT

            return min(a,b,c)

        return dfs(0,0, word1, 0)
