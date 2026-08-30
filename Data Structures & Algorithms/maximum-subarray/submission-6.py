class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def dfs(l,r):
            if l == r:
                return nums[l]
            mid = (l + r )//2
            print(mid)
            left_best = dfs(l, mid)
            right_best = dfs(mid + 1, r)
            left_suffix = float('-inf')
            total = 0
            for i in range(mid,l -1, -1):
                total+=nums[i]
                left_suffix = max(left_suffix, total)
            
            total = 0
            right_suffix = float('-inf')
            for i in range(mid + 1,r + 1):
                total+=nums[i]
                right_suffix = max(right_suffix, total)
            return max(left_best, right_best, right_suffix + left_suffix)
        return dfs(0, len(nums)-1)

