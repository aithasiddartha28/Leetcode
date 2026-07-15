class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path=[]
        ans=[]
        def backtrack(index,total):
            if total==target:
                ans.append(path[:])
                return
            if total>target:
                return
            if index==len(candidates):
                return
            path.append(candidates[index])
            backtrack(index,total+candidates[index])
            path.pop()
            backtrack(index+1,total)
        backtrack(0,0)
        return ans