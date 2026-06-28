import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''n=sorted(nums)
        n1=n[::-1]
        for i in range(len(n1)):
            if k-1==i:
                return n1[i]'''
        
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
