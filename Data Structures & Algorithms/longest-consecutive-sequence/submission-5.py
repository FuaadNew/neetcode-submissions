class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)
        for n in nums:
            if n - 1 not in numsSet:
                length = 1
            
                while n + length in numsSet:
                    length +=1
                longest = max(length,longest)
        return longest
        