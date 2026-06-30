import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        ans=""
        heap=[]
        freq={}
        for  i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for ch,count in freq.items():
            heapq.heappush(heap,(-count,ch))
        while heap:
            count,ch=heapq.heappop(heap)
            count=-count
            ans+=ch*count
        return ans