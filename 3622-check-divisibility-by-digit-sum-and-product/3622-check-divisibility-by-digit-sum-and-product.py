class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        product=1
        temp=n
        while temp>0:
            div=temp%10
            sum+=div
            product*=div
            temp//=10
        total=sum+product
        if n%total==0:
            return True
        return False