class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        i = 0
        j = 0
        res = []
        while i < len(nums):
            # 0 = nums[i] + nums[l] + nums[r]
            #basic algebra
            #(-nums[i]) = nums[l] + nums[r]) --> 
            #nums[i] + nums[l] + nums[r] = 0
            l,r = i + 1, len(nums)-1
            target = -nums[i]
            while l<r:
                candidate = nums[l] + nums[r]
                if candidate  == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
                    
                    while r > 0 and nums[r] == nums[r + 1]:
                        r-=1
                    
                elif candidate < target:
                    l+=1
                else:
                    r-=1
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i+=1
            i+=1
        return res