class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matx = matrix
        self.sumr =[]

        for row in matrix:
            r = []
            s = 0
            for j in range(len(row)):
                s+= row[j]
                r.append(s)
            self.sumr.append(r)

    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s=0
        for j in range(row1, row2+1):
             s+= self.sumr[j][col2] - self.sumr[j][col1] + self.matx[j][col1]

        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)