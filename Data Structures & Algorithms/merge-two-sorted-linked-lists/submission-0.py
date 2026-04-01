# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        if not l1:
            return l2
        elif not l2:
            return l1 

        l3 = min(l1, l2, key=lambda l: l.val)
        head = l3

        if l3 == l1:
            l1 = l1.next
        else:
            l2 = l2.next

        while l1 != None or l2 != None:

            if l1 == None:
                n = l2
            elif l2 == None:
                n = l1
            else:
                n = min(l1, l2, key=lambda l: l.val)
            
            l3.next = n
            l3 = l3.next
            
            if n == l1:
                l1 = l1.next
            else:
                l2 = l2.next
        
        return head

