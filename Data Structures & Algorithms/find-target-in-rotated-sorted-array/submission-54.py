class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l  # Now l is the index of the smallest element
        l,r = 0,len(nums)-1

        # Decide which part of the array to perform binary search on
        if target >= nums[pivot] and target <= nums[r]:
            # Search in the right part of the array (from pivot to right)
            l = pivot
            
        else:
            # Search in the left part of the array (from left to pivot - 1)
            l = 0
            r = pivot - 1

        # Binary search in the chosen part

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

        