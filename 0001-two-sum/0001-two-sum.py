class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''result=[]
        sum=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
        return result'''
        freq={}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in freq:
                return[freq[need],i]
            freq[nums[i]]=i