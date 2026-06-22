class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_to_index = {x:i for i,x in enumerate(nums)}


        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                if num_to_index[complement] == i:
                    continue
                return [i, num_to_index[complement]]

