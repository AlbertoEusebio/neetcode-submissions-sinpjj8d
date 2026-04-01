# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 0
        j = 0

        nodes = []

        s = 0
        while l1 != None or l2 != None:
            
            a = 0
            b = 0

            if l1:
                a = 10 ** i * l1.val
                i += 1
                l1 = l1.next

            if l2:
                b = 10 ** j * l2.val
                j += 1
                l2 = l2.next
        
            s += a + b

        s = str(s)[::-1]

        head = ListNode(int(s[0]))

        n = head
        for c in s[1:]:
            n.next = ListNode(int(c))
            n = n.next
        n.next = None

        return head
