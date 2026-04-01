class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) // 2 + 1

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
            if freq[n] >= maj:
                return n
