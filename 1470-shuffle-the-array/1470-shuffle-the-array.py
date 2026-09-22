class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        res=[]
        for i in range(len(left)):
            ans1=left[i]
            res.append(ans1)
            ans2=right[i]
            res.append(ans2)
            i+=1
        return res