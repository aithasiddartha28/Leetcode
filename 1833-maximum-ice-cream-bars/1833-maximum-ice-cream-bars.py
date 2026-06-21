class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        newarr=sorted(costs)
        sum=0
        count=0
        for i in newarr:
            sum+=i
            if sum<=coins:
                count+=1
        return count