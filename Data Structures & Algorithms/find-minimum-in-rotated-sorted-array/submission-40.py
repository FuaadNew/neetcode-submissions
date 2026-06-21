class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minVal = float('inf')
        while l<=r:
            mid = (l + r)//2
            minVal = min(minVal,nums[mid])
            if nums[l] < nums[r]:
                return min(minVal,nums[l])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return minVal