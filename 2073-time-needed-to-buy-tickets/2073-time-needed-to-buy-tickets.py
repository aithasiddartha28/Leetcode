class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=[]
        count=0
        for i in range(len(tickets)):
            queue.append([tickets[i],i])
        while queue:
            person=queue.pop(0)
            person[0]-=1
            count+=1
            if person[0]==0:
                if person[1]==k:
                    return count
            else:
                queue.append(person)
        '''count=0
        while tickets[k]>0:
            sub=tickets[0]-1
            tickets.pop(0)
            tickets.append(sub)
            count+=1
            if sub==0:
                tickets.pop(sub)
            if k>=0:
                k-=1
            else:
                k==k
            
            
        return count'''