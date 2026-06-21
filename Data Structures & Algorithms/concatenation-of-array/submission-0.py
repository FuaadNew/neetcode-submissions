class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = [0] * (len(nums) * 2)
        n = len(nums)

        for i in range(len(nums)):
            res[i] = nums[i]
            res[i + n] = nums[i]
        return res