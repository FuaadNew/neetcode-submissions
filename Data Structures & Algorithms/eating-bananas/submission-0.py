class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToComplete(k):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            return total_time

        k = 1

        while True:
            if timeToComplete(k) <=h:
                return k
            k+=1
        