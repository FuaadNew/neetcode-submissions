class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subLists = []
        curList = []
        candidates.sort()
        def dfs(i,subLists,curList,total):
            if total == target:
                subLists.append(curList.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curList.append(candidates[i])
            dfs(i+1,subLists,curList,total + candidates[i])
            curList.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,subLists,curList,total)
        dfs(0,subLists,curList,0)
        return subLists

        