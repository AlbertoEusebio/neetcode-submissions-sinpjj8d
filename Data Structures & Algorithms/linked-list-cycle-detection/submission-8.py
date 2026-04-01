# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return False

        f, s = head, head
        
        while f != None and f.next != None:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False