class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic = defaultdict(int)

        for t in trust:
            a, b = t
            dic[b-1] += 1
            dic[a-1] -= 1

        for i in range(n):
            if dic[i] == n-1:
                return i+1
        return -1