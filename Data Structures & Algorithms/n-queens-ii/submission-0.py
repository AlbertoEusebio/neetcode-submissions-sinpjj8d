class Solution:
    def totalNQueens(self, n: int) -> int:
        
        res = 0

        def same_diag(pos, queens):
            for q in queens:
                if abs(pos[0] - q[0]) == abs(pos[1] - q[1]):
                    return True
            return False

        rows = [0] * n

        def dfs(c, queens):

            if c == n:
                return 1
            
            res = 0
            for i in range(n):
                if rows[i]:
                    continue
                if same_diag((i, c), queens):
                    continue
                
                rows[i] = 1
                res += dfs(c+1, queens + [(i, c)])
                rows[i] = 0
            
            return res

        return dfs(0, [])