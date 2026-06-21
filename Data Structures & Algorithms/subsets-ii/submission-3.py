class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curList = []
        res = []
        def dfs(i,curList):
            if i >= len(nums):
                res.append(curList.copy())
                return 
            curList.append(nums[i])
            dfs(i+1,curList)
            curList.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i+=1
            dfs(i+1,curList)
        dfs(0,curList)
        return res