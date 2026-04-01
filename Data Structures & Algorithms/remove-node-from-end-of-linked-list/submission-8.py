# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        if not head.next and n == 1:
            return None
        # find len
        p = head
        l=0
        while p != None:
            l += 1
            p = p.next
        print(l)

        p = head
        i = 0
        while p != None and i+1 < (l-n):
            p = p.next
            i += 1

        print(i)
        if i == 0 and l-n == 0:
            head = head.next
            return head

        p.next = p.next.next
        return head