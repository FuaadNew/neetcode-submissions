class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum = nums[0]

        for i in range(1,len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            res = max(res, cur_sum)
        return res