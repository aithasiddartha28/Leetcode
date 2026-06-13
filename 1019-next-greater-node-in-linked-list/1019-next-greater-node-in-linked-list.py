# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        ans=[0]*len(arr)
        st=[]
        for i in range(len(arr)):
            while st and arr[i]>arr[st[-1]]:
                ans[st.pop()]=arr[i]
            st.append(i)
        return ans