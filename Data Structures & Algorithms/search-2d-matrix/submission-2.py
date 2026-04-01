class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for row in matrix:
            flat += row

        i, j = 0, len(flat) - 1

        start = i + (j-i+1) // 2

        print(flat)
        k = 10
        while i < j and flat[start] != target:
            if flat[start] > target:
                j = start -1
            elif flat[start] < target:
                i = start + 1
            else:
                return True
            
            print(start, i, j, flat[start])
            start = i + (j-i+1) // 2
            k -= 1

        if 0 <= start < len(flat) and flat[start] == target:
            return True
        
        return False