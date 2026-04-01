# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.is_bal = True

        def dfs(node):
            
            if not node:
                return 0

            left_ds = dfs(node.left) + 1
            right_ds = dfs(node.right) + 1

            if abs(right_ds - left_ds) > 1:
                self.is_bal = False
        
            return max(left_ds, right_ds)

        dfs(root)

        return self.is_bal

