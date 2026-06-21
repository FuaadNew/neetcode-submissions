class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        output = []
        for i in range(n - k + 1):
            intervalMax = max(nums[i:i + k])
            output.append(intervalMax)
        return output