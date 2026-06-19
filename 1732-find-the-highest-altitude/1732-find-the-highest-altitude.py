class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr=[]
        arr.append(0)
        arr.append(gain[0])
        for i in range(len(gain)-1):
            sum=arr[-1]+gain[i+1]
            arr.append(sum)
        return max(arr)