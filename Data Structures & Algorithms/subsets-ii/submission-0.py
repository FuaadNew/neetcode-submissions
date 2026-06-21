class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curSet,subSets = [],[]
        nums.sort()
        self.helper2(0,nums,curSet,subSets)
        return subSets

    def helper2(self,i,nums,curSet,subSets):
        if i >= len(nums):
            subSets.append(curSet.copy())
            return
        curSet.append(nums[i])
        self.helper2(i +1,nums,curSet,subSets)
        curSet.pop()

        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        
        self.helper2(i +1,nums,curSet,subSets)
        