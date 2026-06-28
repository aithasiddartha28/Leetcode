class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        a=sorted(arr)
        a[0]=1
        for i in range(1,len(a)):
            if a[i]>a[i-1]+1:
                a[i]=a[i-1]+1
        return a[-1]
                
