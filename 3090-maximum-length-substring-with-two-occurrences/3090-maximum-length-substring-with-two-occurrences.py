class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count={}
        left=0
        ans=0
        for i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            while count[s[i]]>2:
                count[s[left]]-=1
                left+=1
            ans=max(ans,i-left+1)
        return ans