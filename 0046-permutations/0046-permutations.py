class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''res=[]
        if len(nums)==1:
            return [nums.copy()]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res'''
        ans=[]
        path=[]
        user=[False]*len(nums)
        def backtrack():
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if user[i]:
                    continue
                path.append(nums[i])
                user[i]=True
                backtrack()
                path.pop()
                user[i]=False
        backtrack()
        return ans