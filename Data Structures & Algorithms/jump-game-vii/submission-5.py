class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        if s[-1] != '0':
            return False
        
        # if s[-minJump-1] != '0':
        #     return False

        n =len(s)

        lens = [len(i) for i in s.split('0')]
        m_len = max(lens)
        
        if m_len >= maxJump:
            return False
        
        dp = {}
        def dfs(i):
            print(i)
            if i == n-1:
                dp[i] = True
                return True

            if i in dp:
                return dp[i]

            for j in range(i+minJump, i+maxJump+1):
                if j >= n:
                    break
                if s[j] == '0':

                    # if j in dp:
                    #     return dp[j]
                    if dfs(j):
                        dp[j] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)