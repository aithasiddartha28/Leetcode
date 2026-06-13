# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        mx=0
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=mx:
                ans.append(arr[i])
                mx=arr[i]
        ans.reverse()
        dummy = ListNode(0)
        curr = dummy
        for i in ans:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
       