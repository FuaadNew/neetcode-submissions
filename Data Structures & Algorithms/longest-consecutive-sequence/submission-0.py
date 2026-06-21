class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        setter = set(nums)
        for n in nums:
            if (n-1)  not in setter:
                length = 1
                while (n + length) in setter:
                    length +=1
                longest = max(length,longest)
        return longest


        