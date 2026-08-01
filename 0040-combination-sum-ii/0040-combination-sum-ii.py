class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        path=[]
        def backtracking(index,total):
            if total==target:
                ans.append(path[:])
                return
            if total>target:
                return
            if index==len(candidates):
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(i+1,total+candidates[i])
                path.pop()
        backtracking(0,0)
        return ans