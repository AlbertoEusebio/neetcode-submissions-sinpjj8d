# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            l_h = dfs(root.left)
            r_h = dfs(root.right)
            
            res = max(res, l_h + r_h)
            return 1 + max(l_h, r_h)
        
        dfs(root)

        return res