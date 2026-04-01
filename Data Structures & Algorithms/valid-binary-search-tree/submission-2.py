# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = [(root, -1001, 1001)]

        while stack:
            n, mn, mx = stack.pop()

            if n.val <= mn or n.val >= mx:
                return False
        
            if n.right:
                stack.append((n.right, n.val, mx))
            if n.left:
                stack.append((n.left, mn, n.val))

        return True