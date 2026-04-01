class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        visit = [0]*n

        def chk_vis(visited):
            s=0
            sv = 0
            for j,v in enumerate(visited):
                if v:
                    sv += nums[j]
                else:
                    s+= nums[j]
            if s == sv:
                return True

            return False
                                                                                                                                                                                    


        def dfs(i, visit):

            # at each step include or exclude -->2**n solution
            if i>= n:
                # check sum T/F
                return chk_vis(visit)
                            
            # take
            visit[i]=1
            a=dfs(i+1, visit)

            # skip
            visit[i]=0
            b=dfs(i+1, visit)

            return a or b


        return dfs(0, visit)
