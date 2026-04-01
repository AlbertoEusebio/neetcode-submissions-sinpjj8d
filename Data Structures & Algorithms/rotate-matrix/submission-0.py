class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        for i in range(n//2):
            matrix[n-1-i], matrix[i] = matrix[i], matrix[n-1-i]

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                