# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        while root:

            if min_val <= root.val and max_val >= root.val:
                return root
            elif max_val <= root.val:
                root = root.left
            elif min_val >= root.val:
                root = root.right
        
        return root