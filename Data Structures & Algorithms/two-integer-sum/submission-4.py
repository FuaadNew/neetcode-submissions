class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        for i,n in enumerate(nums):
            diffDict[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffDict and diffDict[diff] != i:
                return [i,diffDict[diff]]
            


        