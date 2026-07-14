class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''for i in range(len(nums)):
            for j in range(i,len(nums)):
                print(nums[i:j+1])'''
        ans=[]
        path=[]
        def backtracking(index):
            if index==len(nums):
                ans.append(path[:])
                return
            path.append(nums[index])
            backtracking(index+1)
            path.pop()
            backtracking(index+1)
        backtracking(0)
        return ans