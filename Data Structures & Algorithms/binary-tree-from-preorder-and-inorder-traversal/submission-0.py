# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None

        rval = preorder[0]
        root = TreeNode(rval)

        # Recursive
        # 1 2 4 5   3 6
        # [1] [2 3] [[4 5] [6]]  
        # left   right
        # 4 2 5 1 3 6

        if len(inorder) < 2 or len(preorder) < 2:
            return root

        i = 0
        while inorder[i] != rval:
            i+=1

        # finding index root
        l_pre = preorder[1:i+1]
        r_pre = preorder[i+1:]

        l_in = inorder[:i]
        r_in = inorder[i+1:]

        print(l_pre, r_pre, l_in, r_in)
        root.left = self.buildTree(l_pre, l_in)
        root.right = self.buildTree(r_pre, r_in)

        return root