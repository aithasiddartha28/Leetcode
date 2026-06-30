import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''s=sorted(nums)
        s1=s[::-1]
        res=(s1[1]-1)*(s1[0]-1)
        return res'''

        nums=[-x for x in nums]
        heapq.heapify(nums)
        first=-heapq.heappop(nums)
        secound=-heapq.heappop(nums)
        return (first-1)*(secound-1)