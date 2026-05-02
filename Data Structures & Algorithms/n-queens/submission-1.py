class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        rows = [0] * n
        cols = [0] * n

        def same_diag(queens, pos):
            for q in queens:
                if abs(q[0] - pos[0]) == abs(q[1] - pos[1]):
                    return True
            return False

        def dfs(k, queens):
            nonlocal res
            nonlocal cols, rows

            if len(queens) == n:
                mat = []
                
                for i in range(n):
                    s = ''
                    for j in range(n):
                        if (i, j) in queens:
                            s += 'Q'
                        else:
                            s += '.'
                    mat.append(s)
                
                if mat not in res:
                    res.append(mat.copy())
                return

            for i,r in enumerate(rows):
                if r == 1:
                    continue
                if same_diag(queens, (i, k)):
                    continue

                rows[i] = 1
                cols[k] = 1
                q = (i, k)
                dfs(k+1, queens + [q])
                rows[i] = 0
                cols[k] = 0


        dfs(0, [])
        return res
