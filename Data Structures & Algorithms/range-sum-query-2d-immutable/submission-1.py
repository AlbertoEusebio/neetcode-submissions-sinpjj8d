class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        cols, rows = len(matrix[0]), len(matrix)
        self.sumArr = [[0] * (cols+1) for _ in range(rows+1)]

        for i in range(rows):
            p = 0
            for j in range(cols):
                p += matrix[i][j]
                self.sumArr[i+1][j+1] = p + self.sumArr[i][j+1]
            print(self.sumArr[i+1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
            return self.sumArr[row2+1][col2+1] - self.sumArr[row2+1][col1] - self.sumArr[row1][col2+1] + self.sumArr[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)