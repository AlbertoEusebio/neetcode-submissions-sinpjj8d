class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def area(a, b):
            return min(heights[a], heights[b]) * abs(b-a)


        l, r = 0, len(heights)-1
        max_a = 0

        while l < r:
            a = area(l, r)
            max_a = max(a, max_a)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_a