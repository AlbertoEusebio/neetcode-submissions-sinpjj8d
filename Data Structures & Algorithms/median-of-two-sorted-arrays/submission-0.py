class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        # find min length array
        snums = nums1
        bnums = nums2
        if len(nums1) > len(nums2):
            snums = nums2
            bnums = nums1

        # how many elements on the left
        half = (len(nums1) + len(nums2)) // 2

        # edge case for even numbers: TODO

        l, r = 0, len(snums) - 1 
        while True:
            m = (l+r) // 2
            n = half - m - 2

            sleft = snums[m] if m >= 0 else float('-inf')
            sright = snums[m+1] if (m+1) < len(snums) else float('inf')
            bleft = bnums[n] if n >= 0 else float('-inf')
            bright = bnums[n+1] if (n+1) < len(bnums) else float('inf')

            if sleft <= bright and bleft <= bright:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(sright, bright)
                return (min(sright, bright) + max(sleft, bleft)) / 2
            elif sleft > bright:
                r = m - 1
            else:
                l = m + 1
        
