class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy = set()
        
        for n in nums:
            if n in hashy:
                return True
            else:
                hashy.add(n)
        return False