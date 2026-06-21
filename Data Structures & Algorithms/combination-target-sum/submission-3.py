class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curSet = []
        total = 0

        def dfs(i,curSet,total):
            if total == target:
                res.append(curSet.copy())
                return
            if total > target or i>= len(nums):
                return
            #include current number
            curSet.append(nums[i])
            dfs(i,curSet,total + nums[i])
            #not include current number
            curSet.pop()
            dfs(i+1,curSet,total)
        
        dfs(0,curSet,total)
        return res

        