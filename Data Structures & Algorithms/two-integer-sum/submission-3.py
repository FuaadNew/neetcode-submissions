class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference in hashy:
                return [hashy[difference],i]
            else:
                hashy[n] = i
        

        