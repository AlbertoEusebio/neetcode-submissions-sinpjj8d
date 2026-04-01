# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        if not head:
            return False 

        h = head
        while h.next != None:
            if h in visited:
                return True
            visited.add(h)

            h = h.next
        return False