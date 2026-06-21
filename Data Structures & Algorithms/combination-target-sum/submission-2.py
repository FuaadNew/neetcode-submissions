class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curList = []
        res = []
        total = 0
        def dfs(i,curList,total):
            if total == target:
                res.append(curList.copy())
                return
            if total > target or i >= len(nums):
                return
            curList.append(nums[i])
            dfs(i,curList,total + nums[i])
            curList.pop()
            dfs(i+1,curList,total)
        dfs(0,curList,0)
        return res


        