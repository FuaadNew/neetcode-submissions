class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat = set()

        for n in nums:
            if n in repeat:
                return True
            repeat.add(n)
        return False