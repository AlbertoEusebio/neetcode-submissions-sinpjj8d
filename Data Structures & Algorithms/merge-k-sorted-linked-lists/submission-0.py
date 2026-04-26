# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(-1)
        h = head

        while True:
            mc = -1
            for i in range(len(lists)):
                if lists[i] and (mc == -1 or lists[i].val < lists[mc].val): 
                    mc = i
            
            if mc == -1:
                break

            h.next = lists[mc]
            lists[mc] = lists[mc].next
            h = h.next
        return head.next