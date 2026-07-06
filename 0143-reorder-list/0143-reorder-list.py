# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast and fast.next !=None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow.next
        while curr!=None:
            later=curr.next
            curr.next=prev
            prev=curr
            curr=later
        slow.next=None
        a,b=head,prev
        while b:
            t1=a.next
            t2=b.next
            a.next=b
            b.next=t1
            a=t1
            b=t2

        