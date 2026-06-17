# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        h = head
        i = 0
        while h != None:
            i += 1
            h = h.next

        if n == 0:
            return head.next
        if i == n:
            return head.next

        
        HEAD = ListNode(-1, head)

        h = HEAD.next
        for j in range(i-n-1):
            h = h.next

        h.next = h.next.next

        return HEAD.next