class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) == days:
            return max(weights)
        # elif len(weights) % days != 0:
        #     m = max(weights)
        #     i = 0
        #     for d in range(days):

        def can_ship(mx):
            d = 1
            cap = mx
            for w in weights:
                if cap - w < 0:
                    cap = mx
                    d += 1
                    if d > days:
                        return -1
            
                cap -= w
            return 1

        l,r = max(weights), sum(weights)
        res = r
        m = (l+r) // 2
        while l <= r:
            cs = can_ship(m)
            print(m, cs, l, r)
            # return
            if cs == 1:
                r = m-1
                res = min(m, res)
            elif cs == -1:
                l = m+1
            m = (l+r) // 2
        return res