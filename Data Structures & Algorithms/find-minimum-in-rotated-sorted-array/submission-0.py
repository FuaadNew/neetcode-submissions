class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]

        for n in nums:
            if n < min:
                min = n
        return min
        