from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,4,3,2] -- h= 9
        # at least 4h with k=4
        # k=2 --> 1 + 2 + 2 + 1 = 6h
        # k=1 --> 1 + 4 + 3 + 2 = 10h

        max_ban = max(piles)
        
        if len(piles) == h:
            return max_ban

        i, j = 1, max_ban

        k = i + (j-i) // 2

        k_p = k 
        while i<j:
    
            hours = sum([ceil(p / k) for p in piles])

            print(i, j, k, hours)

            if hours <= h:
                j = k - 1
                k_p = k
            elif hours > h:
                i = k + 1

            k = i + (j-i) // 2 

        print(i, j, k, hours)

        hours = sum([ceil(p / k) for p in piles])
        if hours <= h:
            return k

        return k_p
        