class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        
        
        while l<r:
            timeToEat = 0
            
            k = (l + r)//2
            for p in piles:
                timeToEat+= math.ceil(p/k)
            if timeToEat > h:
                l = k + 1
            elif timeToEat <= h:
                r = k
        return l


        
        