class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(x):
            if x > n:
                return 0
            if x == n:
                return 1
            return dfs(x + 1) + dfs(x+2)
        return dfs(0)