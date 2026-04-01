class Solution:
    def rob(self, nums: List[int]) -> int:
        # start at 0 or at 1 

        n = len(nums)
        pre_comp = [-1] * (n+2)

        def dfs(i, rob):
            if i >= n:
                return rob
            rob += nums[i]
            
            print(pre_comp, i, rob)
            m = [0]
            for j in range(i+2, n):
                a = pre_comp[j] if pre_comp[j] != -1 else (dfs(j, rob) - rob)
                m.append(a)

            pre_comp[i] = max(m) + nums[i]

            return max(m) + rob


        comp = [0]
        for j in range(0, n):
            a = pre_comp[j] if pre_comp[j] != -1 else dfs(j, 0)
            comp.append(a)

        return max(comp)