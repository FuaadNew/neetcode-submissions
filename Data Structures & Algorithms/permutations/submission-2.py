class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curList = []
        res = []
        def dfs():
            if len(curList) == len(nums):
                res.append(curList.copy())
                return
            for n in nums:
                if n not in curList:
                    curList.append(n)
                    dfs()
                    curList.pop()
        dfs()
        return res
        