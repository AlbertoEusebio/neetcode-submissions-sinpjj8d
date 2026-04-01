# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return

        t = head

        l1 = head
        l2 = head

        while l2 != None and l2.next != None:
            # print(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next.next

        # Reached half list with l
        # now reverse half - list 
        # 1, 2, 3, 4, 5
        t = l1
        while t.next != None:
            t = t.next
        
        #### Separate 2 lists
        k = head
        while k.next != l1:
            k = k.next 
        k.next = None

        while l1 != t:
            tmp = l1.next
            l1.next = t.next
            t.next = l1
            l1 = tmp

        l2 = head # restore

        c = l1
        while c.next != None:
            print(c.val)
            c = c.next
        print(c.val)
        c.next = None

        while l1 != None and l2 != None:
            # print(l2.val, l1.val)
            tmp = l2.next
            l2.next = l1
            tmp2 = l1.next
            l1.next = tmp
            l1 = tmp2
            l2 = tmp

        t = head
        while t.next != None:
            t = t.next
        
        while l1 != None:
            t.next = l1
            l1 = l1.next
            t = t.next