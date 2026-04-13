class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}

        for c in bills:
            chg = c - 5
            change[c] += 1 

            if chg == 0:
                continue

            for a in [20, 10, 5]:
                while change[a] and chg >= a:
                    # print(chg, change, a)
                    chg -= a
                    change[a] -= 1


            if chg != 0:
                return False
        return True
