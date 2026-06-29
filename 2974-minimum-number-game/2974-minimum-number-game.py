class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        s=sorted(nums)
        s1=s[::-1]
        while s1:
            a=s1.pop()
            b=s1.pop()
            arr.append(b)
            arr.append(a)
        return arr
