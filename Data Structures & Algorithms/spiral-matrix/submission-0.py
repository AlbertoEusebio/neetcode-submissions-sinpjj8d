class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix)
        m = len(matrix[0])

        l,r,t,b = 0, m, 0, n

        res = []

        print(res,l,r,t,b)

        while l<r and t <b:
            print('start')
            for i in range(l, r):
                res.append(matrix[t][i])
            t +=1
            print(res,l,r,t,b)

            if not (l<r and t <b):
                break

            for i in range(t, b):
                res.append(matrix[i][r-1])
            r -= 1
            print(res,l,r,t,b)

            if not (l<r and t <b):
                break

            for i in range(r-1, l-1, -1):
                res.append(matrix[b-1][i])
            b -= 1
            print(res,l,r,t,b)

            if not (l<r and t <b):
                break

            for i in range(b-1, t-1, -1):
                res.append(matrix[i][l])
            l += 1
        
            print(res,l,r,t,b, 'end')

        return res