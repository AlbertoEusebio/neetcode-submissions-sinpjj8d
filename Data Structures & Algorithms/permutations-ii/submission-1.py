class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        pick = [0] * len(freq.keys())

        res = []
        def dfs(freq, pth):
            nonlocal res
            if len(pth) == len(nums):
                res.append(pth.copy())
                return

            for k in freq.keys():
                if freq[k] == 0:
                    continue
                freq[k] -= 1
                dfs(freq, pth + [k])
                freq[k] += 1

        dfs(freq, [])
        return res