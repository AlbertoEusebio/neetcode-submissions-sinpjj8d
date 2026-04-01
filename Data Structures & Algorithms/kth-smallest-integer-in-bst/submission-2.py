# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.ret = -1
        self.cnt = k
        def dfs(n):

            if not n:
                return
            dfs(n.left)
            self.cnt -= 1

            if self.cnt == 0:
                self.ret = n.val
                return
            
            dfs(n.right)
        
        dfs(root)
        return self.ret
            