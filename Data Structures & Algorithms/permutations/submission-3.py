class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curSet = []
        res = []
        def dfs():
            if len(curSet) == len(nums):
                res.append(curSet.copy())
            
            for n in nums:
                if n not in curSet:
                    curSet.append(n)
                    dfs()
                    curSet.pop()
        dfs()
        return res



        