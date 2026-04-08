class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)

        if s %4 != 0:
            return False
        
        if len(matchsticks) < 4:
            return False

        l = s // 4


        matchsticks = sorted(matchsticks, reverse=True)
        for m in matchsticks:
            if m > l:
                return False
        
        sides = [0,0,0,0]

        def dfs(i):
            # at each take or not

            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            # if there is a solution, there is a side where to put the stick
            for j in range(4):
                if sides[j] + matchsticks[i] > l:
                    continue
                sides[j] += matchsticks[i]
                if dfs(i+1):
                    return True
                sides[j] -= matchsticks[i]
                
            return False
        return dfs(0)