class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(path, remain, l):

            print(path, remain, l)          
            if len(remain) == 0:
                res.append(path.copy())
                return

            for i in range(len(remain)):
                n = remain[i]
                rem = remain[:i] + remain[i+1:]
                path.append(n)
                dfs(path.copy(), rem.copy(), l+1)
                path.pop()
        
        dfs([], nums.copy(), 0)

        return res
