class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tmax = []

        n, m = len(matrix), len(matrix[0])

        for j in range(m):
            row = []
            for i in range(n):
                row.append(matrix[i][j])
            tmax.append(row)
        return tmax
