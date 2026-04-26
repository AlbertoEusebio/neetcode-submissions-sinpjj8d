class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        # binary search
        i,j = 0, len(self.nums) - 1

        if len(self.nums) == 0:
            self.nums.append(num)
            return

        if num >= self.nums[-1]:
            self.nums.append(num)
            return
        elif num <= self.nums[0]:
            self.nums = [num] + self.nums
            return

        while i < j:
            m = (i+j) // 2

            if num > self.nums[m]:
                i = m+1
            else:
                j = m-1
        
        # 1 3 - 1
        print(m)
        if self.nums[m] < num:
            self.nums = self.nums[:m+1] + [num] + self.nums[m+1:]
        else:
            self.nums = self.nums[:m] + [num] + self.nums[m:]

    def findMedian(self) -> float:
        m = len(self.nums)
        print(self.nums)
        if m % 2 == 0:
            n = m // 2 - 1
            return (self.nums[n] + self.nums[n+1]) / 2
        
        return self.nums[m//2]