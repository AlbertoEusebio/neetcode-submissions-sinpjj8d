from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for a in asteroids:
            if res == []:
                res.append(a)
                continue
            else:
                while res:
                    add_ = False
                    n = res.pop()
                    if a < 0 and n > 0:
                        if abs(a) < abs(n):
                            res.append(n)
                            break
                        elif abs(a) == abs(n):
                            break
                        else:
                            add_ = True
                    else:
                        res.append(n)
                        res.append(a)
                        break
                if add_:
                    res.append(a)
        return res