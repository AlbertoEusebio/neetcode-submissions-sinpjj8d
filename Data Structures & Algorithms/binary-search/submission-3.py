class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = nums
        i, j = 0, len(nums)-1

        start = i + (j-i+1) // 2
        k = 10
        while n[start] != target and i < j:
            print(i, j, start)

            if n[start] > target:
                # move left
                j = start-1
            elif n[start] < target:
                i = start+1
            
            k-=1

            start = i + (j-i+1) // 2
            if start < 0 or start > len(nums) -1:
                return -1

        if i==j:
            if n[start] == target:
                return start
            return -1

        return start