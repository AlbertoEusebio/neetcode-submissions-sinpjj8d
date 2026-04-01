from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        nums = set(nums)

        res = [[]]
        stack = []
        stack.append([])
        stack.append(nums)

        while stack:
            arr = stack.pop()
            larr = list(arr)
            if len(larr) and larr not in res:
                res.append(larr)
            else:
                continue

            for i in arr:
                stack.append(arr - set([i]))

        return list(res)