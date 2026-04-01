class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        def dfs(x, n):

            if n == 1:
                return x

            if n == 2:
                return x*x
            

            if x == 0:
                if n == 0:
                    return 1
                return x

            a = n // 2
            b = n - n//2

            return dfs(x, a) * dfs(x, b)

        s = n / abs(n)
        
        if s == 1:
            return dfs(x, abs(n))
        
        return 1/dfs(x, abs(n))
