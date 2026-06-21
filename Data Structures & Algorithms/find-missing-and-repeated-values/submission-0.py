class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flatten = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                flatten.append(grid[r][c])
        
        nums = []

        for flat in flatten:
            if flat in nums:
                repeat = flat
            nums.append(flat)
        missing = 0

        for i in range(1,len(nums)+1):
            print(i)
            if i not in nums:
                missing = i
        return [repeat, missing]
            