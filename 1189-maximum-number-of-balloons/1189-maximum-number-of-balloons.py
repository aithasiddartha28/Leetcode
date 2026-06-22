class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word="balloon"
        fre={}
        for i in text:
            if i in fre:
                fre[i]+=1
            else:
                fre[i]=1
        a=float("inf")
        for j in word:
            if j in fre:
                value=fre[j]//word.count(j)
            else:
                value=0
            if value<a:
                a=value
        return a
            