class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = set()
        cols = set()

        for i in range(len(matrix)):
            print(matrix[i])
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        print(rows)
        print(cols)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        