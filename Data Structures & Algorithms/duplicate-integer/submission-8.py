class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = set()
        for num in nums:
            if num in hashy:
                return True
            else:
                hashy.add(num)
        return False
         