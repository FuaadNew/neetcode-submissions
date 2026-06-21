class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        minTime = max(piles)
        while l<=r:
            k = (l + r) // 2
            timetoEat = 0
            for p in piles:
                timetoEat+= math.ceil(p/k)
            if timetoEat <= h:
                minTime = min(minTime,k)
                r = k - 1
            else:
                l = k + 1
        return minTime


            
            

        