# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse_k(head):
            i = 0
            h = head
            while h.next is not None and i < k:
                h = h.next
                i += 1
            tail = h

            if i < k:
                return

            h = head.next
            nxt_tail = head.next
            for i in range(k-1):
                buff1 = tail.next
                buff2 = h.next
                h.next = buff1
                tail.next = h
                h = buff2
            head.next = tail
        
        H = ListNode(-1)
        H.next = head

        reverting_heads = [H]
        
        h = H
        i = 0
        while h.next is not None:
            i += 1
            h = h.next 

            if i % k == 0:
                reverting_heads.append(h)

        while reverting_heads:
            h = reverting_heads.pop()
            reverse_k(h)

        return H.next