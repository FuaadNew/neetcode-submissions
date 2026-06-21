class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = []
        for n in nums:
            if n in hashy:
                return True
            else:
                hashy.append(n)
        return False