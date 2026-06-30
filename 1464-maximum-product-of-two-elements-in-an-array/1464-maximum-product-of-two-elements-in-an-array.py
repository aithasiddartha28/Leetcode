class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        s=sorted(nums)
        s1=s[::-1]
        res=(s1[1]-1)*(s1[0]-1)
        return res