# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        while current and current.next:
            value=gcd(current.val,current.next.val)
            new_node=ListNode(value)
            new_node.next=current.next
            current.next=new_node
            current=current.next.next
        return head