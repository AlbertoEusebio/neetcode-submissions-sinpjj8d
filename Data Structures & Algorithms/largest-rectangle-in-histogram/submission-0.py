class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            #
        #   #
        # # #
        ######

        stack = []
        area = 0

        for i, h in enumerate(heights + [0]):

            j = i
            while stack and stack[-1][1] > h:
                j, v = stack.pop()
                a = (i-j) * v
                # print(i,j, a)
                area = max(area, a)

            stack.append((j, h))
        
        print(stack)
        return area