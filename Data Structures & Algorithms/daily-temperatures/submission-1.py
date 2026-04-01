class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        res = [0] * len(temperatures)

        # [30,38,30,36,35,40,28]
        # [1, 4, 1, 2, 1, 0, 0]
        # [5, 6]

        for i, t in enumerate(temperatures):
            print(stack)
            if stack and t > temperatures[stack[-1]]:
                while stack != [] and temperatures[stack[-1]] < t:
                    p = stack.pop()
                    res[p] = i - p
            stack.append(i)
        return res
