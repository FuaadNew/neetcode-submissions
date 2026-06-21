class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subSets = []

        def dfs(i):
            if i >= len(nums):
                res.append(subSets.copy())
                return
            
            subSets.append(nums[i])
            dfs(i+1)

            subSets.pop()
            dfs(i+1)
        dfs(0)
        return res


        