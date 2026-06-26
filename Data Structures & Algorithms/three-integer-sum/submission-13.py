class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i = 0
        print(nums)
        res = []
        #[-2, 0, 1, 1, 2]
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i+=1
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r]
                if curSum == -nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
                    while l < r and nums[r] == nums[r + 1]:
                        r-=1
                elif curSum < -nums[i]:
                    l+=1
                else:
                    r-=1
                

            i+=1

        return res





            
            