class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
        return maxP