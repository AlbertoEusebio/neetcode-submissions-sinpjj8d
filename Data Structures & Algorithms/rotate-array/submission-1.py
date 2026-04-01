class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        clone = nums.copy()
        n = len(nums)
        k = k % n 
        nums[:k] = nums[n-k:]
        # print(nums)
        nums[k:] = clone[:n-k]
