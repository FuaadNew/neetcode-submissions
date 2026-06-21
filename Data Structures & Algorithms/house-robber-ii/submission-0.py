class Solution:
    def rob(self, nums: List[int]) -> int:
        #call helper function skipping first house
        #call helper function skipping last house
        #get the max of the two values, plus edge case of only one value
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    
    def helper(self,nums):
        rob1,rob2 = 0,0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        
    
    