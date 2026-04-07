# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(r):

            if r is None:
                return None

            r.left = dfs(r.left)
            r.right = dfs(r.right)

            if r.left is None and r.right is None and r.val == target:
                return None
            return r

        return dfs(root)