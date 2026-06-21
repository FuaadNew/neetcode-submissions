class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curSets = []
        subSets = []
        nums.sort()
        def dfs(i,curSets,subSets,nums):
            if i>= len(nums):
                subSets.append(curSets.copy())
                return
            curSets.append(nums[i])
            dfs(i+1,curSets,subSets,nums)
            curSets.pop()
            while i+1 < len(nums) and nums[i] == nums[i + 1]:
                i+=1
            dfs(i+1,curSets,subSets,nums)
        dfs(0,curSets,subSets,nums)
        return subSets
        