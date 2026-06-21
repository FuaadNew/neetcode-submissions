class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = []

        for n in nums:
            if n in mapper:
                return True
            else:
                mapper.append(n)
        return False
         