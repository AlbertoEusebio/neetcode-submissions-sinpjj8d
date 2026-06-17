# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        HEAD = ListNode(-1, head)
        tail = head

        i = 1
        while tail.next != None:
            i += 1
            tail = tail.next

        while HEAD.next is not None and HEAD.next != tail:
            tmp = tail.next
            tmp2 = HEAD.next.next
            tail.next = HEAD.next
            HEAD.next.next = tmp
            HEAD.next = tmp2
        
        return HEAD.next
