# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        dp = {}

        def dfs(r, skip):
            # at each pos it can rob left or right
            nonlocal dp

            if r is None:
                return 0

            if (r, skip) in dp:
                return dp[(r, skip)]

            # can skip or take. If take skip next
            if skip:
                dp[(r, skip)] = dfs(r.left, False) + dfs(r.right, False)
                return dp[(r, skip)]
            
            a = dfs(r.left, False) + dfs(r.right, False) 
            b = dfs(r.left, True) + dfs(r.right, True) + r.val
            print(r.val, a, b)

            dp[(r, skip)] = max(a, b)


            # take or skip
            return dp[(r, skip)]

        return dfs(root, False)