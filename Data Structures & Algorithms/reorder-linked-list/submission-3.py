# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        h = head
        n = 0
        while h.next is not None:
            h = h.next
            n += 1        
        n+=1
        tail = h

        if n == 1:
            return

        # get to half
        h = head
        half = n // 2
        for i in range(half - 1):
            h = h.next
        
        # reverse second half of linked list
        while tail != h.next:
            tmp = tail.next
            tmp2 = h.next.next
            tail.next = h.next
            tail.next.next = tmp
            h.next = tmp2
        
        l1 = head
        l2 = h.next

        h.next = None

        while l1.next is not None and l2 is not None:
            tmp = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = tmp
            l1 = tmp
        
        if l1.next is None and l2 is not None:
            l1.next = l2
        