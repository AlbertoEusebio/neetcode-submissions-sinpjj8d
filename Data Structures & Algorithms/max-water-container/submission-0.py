class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(h1, h2, l):
            return min(h1, h2) * l
        
        i,j = 0, len(heights) - 1
        nums = heights
        a = 0
        max_a = a

        while i < j:
            a = area(nums[i], nums[j], j - i) 
            if nums[i] >= nums[j]:
                j -= 1
            elif nums[i] < nums[j]:
                i += 1

            if max_a < a:
                max_a = a
        return max_a    
