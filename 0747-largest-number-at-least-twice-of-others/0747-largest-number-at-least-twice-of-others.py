class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        larger=max(nums)
        index=nums.index(larger)
        for i in range(len(nums)):
            if i !=index and larger<2*nums[i]:
                return -1
        return index