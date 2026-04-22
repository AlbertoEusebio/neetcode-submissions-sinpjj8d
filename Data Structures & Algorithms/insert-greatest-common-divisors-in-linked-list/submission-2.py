# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def divisors(n) -> Set[int]:
            divisors = set([n])
            i = n
            while i != 0:
                if n % i == 0:
                    divisors.add(i)
                i -= 1
            return divisors

        def gcd(a, b):
            # See Euclidean algorithm
            while b > 0:
                a, b = b, a % b
            return a



        h = head

        while h.next is not None:
            a, b, nx = h.val, h.next.val, h.next

            gcd = max(divisors(a).intersection(divisors(b))) # n*m operation

            nw = ListNode(gcd, nx)
            h.next = nw
            h = nx
        return head