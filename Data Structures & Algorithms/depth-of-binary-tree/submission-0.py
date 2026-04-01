# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        d_l = self.maxDepth(root.left)
        d_r = self.maxDepth(root.right)

        return max(d_l, d_r) + 1