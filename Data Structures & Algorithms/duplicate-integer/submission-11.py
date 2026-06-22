class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat = set(nums)
        if len(repeat) < len(nums):
            return True
        return False