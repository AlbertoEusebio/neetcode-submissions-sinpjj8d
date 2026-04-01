class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = max(len(text1), len(text2))
        m = min(len(text1), len(text2))
        if len(text1) >= len(text2):
            text_max = text1
            text_min = text2
        else:
            text_max = text2
            text_min = text1

        if text_min in text_max:
            return len(text_min)


        memo = {}

        def dfs(i, j):

            if i >= n or j>=m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            print(text_max[i], text_min[j])
    
            b = 0
            if text_max[i] == text_min[j]:
                # take
                b = dfs(i+1, j+1) + 1
                memo[(i, j)] = b
                return b
            else:
                a = dfs(i+1, j) # no take, same char
                c = dfs(i, j+1) # skip char, no take
                memo[(i, j)] = max(a, c)
                return max(a, b, c)

        return dfs(0, 0)