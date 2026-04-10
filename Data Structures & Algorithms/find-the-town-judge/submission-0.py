class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [0] * n
        trusts_many = [0] * n

        for t in trust:
            a, b = t
            trusted_by[b-1] += 1
            trusts_many[a-1] += 1
        
        print(trusted_by)
        print(trusts_many)

        for i in range(n):
            if trusts_many[i] == 0 and trusted_by[i] == n-1:
                return i+1
        return -1