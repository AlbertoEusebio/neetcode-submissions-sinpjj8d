class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # 1 2 3 4 3 2 1
        # 1 2 7 5 3 2 1
        # 1 2 3 5 7 2 1

        # Find mountain, split in left and right and search there
        # to find mountain check locally

        # find mountain index
        n = mountainArr.length()

        def up_down(i):
            if i > 0 and i < n-1:
                if mountainArr.get(i-1) < mountainArr.get(i) < mountainArr.get(i+1):
                    return 1
                elif mountainArr.get(i-1) > mountainArr.get(i) > mountainArr.get(i+1):
                    return -1
                else:
                     return 0 # mountain

            if i == 0:
                if mountainArr.get(i) < mountainArr.get(i+1):
                    return 1
                else:
                    return 0 # mountain is 0

            if i == n-1:
                if mountainArr.get(i) > mountainArr.get(i-1):
                    return 0 # peak 
                else:
                    return -1 # mountain is 0

        l, r = 0, n-1
        peak = None

        while l <= r:
            i = (l+r) // 2

            v = up_down(i)

            if v == 0:
                peak = i
                break
            elif v == 1:
                l = i+1
            else:
                r = i-1
        

        # found peak, now we first search left or right
        # we know they are sorted for sure
        # in the def we know there is no repeted number in the 2 sub so when we find target, we know it is the smallest

        l, r = 0, peak

        while l <= r:
            i = (l+r) // 2

            v = mountainArr.get(i)

            if v == target:
                return i
            elif v > target:
                r = i-1
            else:
                l = i+1

        # search largest

        l, r = peak+1, n-1 

        while l <= r:
            i = (l+r) // 2

            v = mountainArr.get(i)

            if v == target:
                return i
            elif v > target:
                l = i+1
            else:
                r = i-1
        
        return -1
        