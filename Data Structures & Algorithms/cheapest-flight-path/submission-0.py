class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #create array with len n with infinity
        prices = [float('inf')] * n
        #except source node is 0
        prices[src] = 0

        #iterate k + 1 times
        for i in range(k+1):
            #create temporary prices array which is a copy
            tmpPrices = prices.copy()
            #go throguh the three values  in flight array
            #source, destination, price
            for s,d, p, in flights:
                #if prices at source node is infinity continue the loop
                if prices[s] == float('inf'):
                    continue
                #if we found a new shortest path s + p to tmpPrices[d]
                #update tmpPrices[d] to prices[s] + p
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            #update prices to be tmpPrices
            prices = tmpPrices
        #return prices of dst if not equal to infintiy else -1
        return -1 if prices[dst] == float('inf') else prices[dst]


        