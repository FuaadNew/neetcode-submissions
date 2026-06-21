class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #cache will start at 1,length of the array
        LIS = [1] * len(nums)
        

        #go through every index in range input array in reverse order
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1 + LIS[j])
        return max(LIS)
        
            #starting at every i iterate through every subsequence
            
                # is the value at i smaller than j
                
                    #update the LIS at index i with the max of itself or 1 + j
                    
                   
        #return the max of the list
        




        