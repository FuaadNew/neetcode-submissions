class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        def count(ele):
            res = 0

            for num in nums:
                if num == ele:
                    res+=1
            return res
        
        res = []
        visit = set()
        n = len(nums)
        for num in nums:
            if num in visit:
                continue
            appear = count(num)
            if appear > n/3:
                res.append(num)
            visit.add(num)
        return res
