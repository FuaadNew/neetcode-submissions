class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = 0
        while l<=r:
            timeToEat = 0
            k = (l + r) //2
            for p in piles:
                timeToEat += math.ceil(p/k)
            if timeToEat <=h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res
        