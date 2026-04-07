# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def append(h, carry):
            if h is None:
                 return h

            if h.right is None:
                h.right = carry
            else:
                h.right = append(h.right, carry)

            return h

        def find(h, k):

            if h is None:
                return None
            
            # k can be a leaf, root or intermediate node

            if h.val == k:
                l = h.left
                r = h.right

                if l is None and r is None: # leaf
                    return None
                # only one available
                elif l is None and r is not None:
                    return r
                elif l is not None and r is None:
                    return l
                else: # both not none
                    cur = l
                    while cur.right:
                        cur = cur.right
                    cur.right = r
                    return l
            elif h.val > k:
                h.left = find(h.left, k)
            else:
                h.right = find(h.right, k)
            
            return h

        return find(root, key)
