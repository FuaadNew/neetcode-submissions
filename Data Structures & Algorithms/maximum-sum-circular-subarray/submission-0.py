class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        res = nums[0]
        n = len(nums)
        for start in range(n):
            cur_sum = 0
            for length in range(n):
                index = (start + length) % n
                cur_sum+= nums[index]
                res = max(res, cur_sum)
        return res