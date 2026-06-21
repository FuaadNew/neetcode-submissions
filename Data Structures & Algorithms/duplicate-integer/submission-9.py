class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        DupliSet = set()
        for n in nums:
            if n in DupliSet:
                return True
            
            DupliSet.add(n)
        return False