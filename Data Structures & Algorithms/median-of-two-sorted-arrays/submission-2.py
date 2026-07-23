class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = nums1 + nums2
        new_arr.sort()

        if len(new_arr) % 2 == 1:
            return new_arr[(math.ceil(len(new_arr)//2))]
        else:
            mid_point = len(new_arr)//2
            return (new_arr[mid_point] + new_arr[mid_point-1]) /2