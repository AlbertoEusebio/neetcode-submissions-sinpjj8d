# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # h              t
        # 1 -> 2 -> 3 -> 4
        # p         t
        # 2 -> 3 -> 4 -> 1
        # 3 -> 4 -> 2 -> 1
        if head == None or head.next == None:
            return head

        h = head
        while h.next != None:
            h = h.next
        
        tail = h

        t = tail
        p = head
        while p != t:
            tmp = p.next
            p.next = t.next
            t.next = p
            p = tmp
        return p
