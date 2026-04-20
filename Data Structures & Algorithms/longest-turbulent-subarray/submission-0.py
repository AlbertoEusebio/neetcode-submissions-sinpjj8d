class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        if len(arr) < 2:
            return len(arr)

        max_l = 0
        l = 0
        for i in range(1, len(arr)):
            if i%2 == 0:
                if arr[i] > arr[i-1]:
                    l += 1
                else:
                    l = 0
            else:
                if arr[i] < arr[i-1]:
                    l += 1
                else:
                    l = 0

            print(arr[i], l)
            if l > max_l:
                max_l = l

        l = 0
        for i in range(1, len(arr)):
            if i%2 == 0:
                if arr[i] < arr[i-1]:
                    l += 1
                else:
                    l = 0
            else:
                if arr[i] > arr[i-1]:
                    l += 1
                else:
                    l = 0
            print(arr[i], l)
            
            if l > max_l:
                max_l = l
        
        return max_l + 1