# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        h = head
        p = ListNode(-1, head)
        i = 1
        while i < left:
            # print(h.val)
            p = h
            h = h.next
            i += 1
        # p is the previous
        l = h
        print(l.val, p.val)

        while i < right:
            # print(h.val)
            h= h.next
            i+=1
        r = h
        print(r.val)

        while l != r:
            tmp = r.next
            tmp2 = l.next
            l.next = tmp
            r.next = l
            l = tmp2
            p.next = l

        return p.next if left == 1 else head