class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i,subsets):
            if len(subsets) == k:
                res.append(subsets[:])
                return
            if i > n:
                return
            subsets.append(i)
            dfs(i+1,subsets)
            
            subsets.pop()
            dfs(i+1,subsets)
        dfs(1,[])
        return res