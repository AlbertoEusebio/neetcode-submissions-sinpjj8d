class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur = deque([])
        res =[]
        for i in range(k):
            cur.append(nums[i])
        res.append(max(cur))
        mx = res[-1]
        for i in range(k, len(nums)):
            a = nums[i]
            cur.popleft()
            cur.append(a)
            res.append(max(cur))

        return res