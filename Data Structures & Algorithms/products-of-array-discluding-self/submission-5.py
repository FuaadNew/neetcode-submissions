class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,post = [0] * len(nums),[0] * len(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(i+1, len(nums)):
                product*= nums[j]
            post[i] = product

        for i in range(len(nums)-1,-1,-1):
            product = 1
            for j in range(i):
                product*= nums[j]
            pre[i] = product
        
        for i in range(len(nums)):
            post[i] = post[i] * pre[i]
        return post

            

             