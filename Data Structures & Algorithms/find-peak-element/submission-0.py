class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l <=r:
            mid = (l + r) //2
            left_neighbor = float('-inf')
            right_neighbor = float('-inf')
            print(nums[mid])
            if mid != 0:
                left_neighbor = nums[mid-1]
            if mid != len(nums)-1:
                right_neighbor = nums[mid + 1]
            if nums[mid] > left_neighbor and nums[mid] > right_neighbor:
                return mid
            
            #are we in the part of the part of the array that is increasing
            if left_neighbor < nums[mid] < right_neighbor:
                l = mid + 1
            else:
                r = mid - 1
