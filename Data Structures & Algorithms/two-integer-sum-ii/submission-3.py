class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # all numbers greater than target are discarded
        j, i = 0, len(numbers) - 1
        while i > j and numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                i -= 1
            else:
                j += 1

        return [j+1, i+1]
