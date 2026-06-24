class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        for i in range(len(numbers)):
            candidate = numbers[i]
            
            l,r = i + 1, len(numbers)-1

            while l<=r:
                mid = (l + r)//2
                curSum = numbers[mid] + candidate

                if curSum == target:
                    return [i + 1, mid + 1]
                
                elif curSum < target:
                    l+=1
                
                else:
                    r-=1
        



