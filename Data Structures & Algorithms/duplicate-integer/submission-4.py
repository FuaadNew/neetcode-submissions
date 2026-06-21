class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = set()
        for n in nums:
            if n in mapper:
                return True
            else:
                mapper.add(n)
        return False
        
         