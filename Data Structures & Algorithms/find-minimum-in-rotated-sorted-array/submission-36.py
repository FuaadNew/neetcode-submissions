class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        res = float('inf')
        while l<=r:
            mid = (l + r)//2
            res = min(res,nums[mid])
            if nums[l] <= nums[r]:
                return min(res,nums[l])
            if nums[mid] >= nums[l]:
                l= mid + 1
            else:
                r = mid -1
            

        