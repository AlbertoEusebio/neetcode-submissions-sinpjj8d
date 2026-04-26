# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path = float('-inf')

        def dfs(r):
            nonlocal max_path

            if r is None:
                return float('-inf')

            v = r.val
            rght = max(dfs(r.right), 0)
            lft = max(dfs(r.left), 0)
            
            mx_loc = lft + rght + v
            max_path = max(max_path, mx_loc)

            return v + max(lft, rght)

        res = dfs(root)
        print(res, max_path)


        return max(res, max_path)