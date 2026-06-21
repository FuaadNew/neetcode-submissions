class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashy = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hashy:
                return [hashy[diff] + 1,i + 1]
            else:
                hashy[n] = i

        


        