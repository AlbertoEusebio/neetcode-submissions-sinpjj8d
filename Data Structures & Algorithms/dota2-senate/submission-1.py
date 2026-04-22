class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r,d = 0, 0
        n = len(senate)
        vote = [1]*n    # all can vote

        countr, countd = 0, 0
        for i,s in enumerate(senate):
            if s == 'R':
                countr+=1
            else:
                countd+=1 

        i = 0
        while countd and countr:
            if vote[i] == 0:
                i += 1
                i%=n
                continue

            s = senate[i]
            # increm var and decrement by shouting when you see the other letter
            if s == 'R':
                if d == 0:
                   r += 1
                else:
                    vote[i] = 0 # shut
                    countr -= 1
                    d -= 1
            elif s == 'D':
                if r == 0:
                    d += 1
                else:
                    vote[i] = 0 # shut
                    countd -= 1
                    r -= 1
            # stopping when all of one group whas removed
            i += 1
            i %= n
        if countr > 0:
            return 'Radiant'
        return 'Dire'