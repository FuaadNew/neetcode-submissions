class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive =[]
        negative = []

        for n in nums:
            if n < 0:
                negative.append(n)
            else:
                positive.append(n)
        
        Flag = True
        posi = 0
        negi = 0
        for i in range(len(nums)):
            if Flag:
                nums[i] = positive[posi]
                posi+=1
                Flag = False
            else:
                nums[i] = negative[negi]
                negi+=1
                Flag = True
        
        return nums

            

