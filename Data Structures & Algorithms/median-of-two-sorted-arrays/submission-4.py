class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       

        A,B = nums1,nums2
        if len(A) > len(B):
            A,B = B,A
        l1 = l2 = 0
        previous = current = 0
        for i in range((len(nums1) + len(nums2))//2 + 1):
            previous = current
            if l1 < len(A) and (l2 >= len(B) or A[l1] <= B[l2]):
                current = A[l1]
                l1+=1
            else:
                
                current = B[l2]
                l2+=1
             
        if (len(A) + len(B)) % 2:
            return float(current)
           
        else:
            return (current + previous) / 2
        



