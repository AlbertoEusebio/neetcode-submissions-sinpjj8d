class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open and close
        # open before close

        res = []

        def dfs(s, n, close):

            if n == 0 and close == 0:
                res.append(s)
                return

            # at each step you can decide to open or to close
            # open means n -= 1 and add '('
            # close means only ')'
            # every open must be closed
            print(s, n)

            # open
            if n > 0:
                dfs(s + '(', n-1, close + 1)

            # close
            if close > 0:
                dfs(s + ')', n, close - 1)

        dfs('', n, 0)

        return res