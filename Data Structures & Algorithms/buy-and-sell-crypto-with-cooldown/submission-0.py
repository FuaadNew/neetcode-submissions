class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp dictionary
        dp = {}
        #recursive function dfs
        #pass i, and buying
        def dfs(i,buying):
            #base case 
            #if index out of bound
            #return 
            if i >= len(prices):
                return 0
            #if parameters already in dp
            if (i,buying) in dp:
                return dp[(i,buying)]
            #decision if we're buying or sellinfg
            #if buying we can buy  or cooldown
            
            if buying:
                #if we buy call buy = dfs on i + 1
                #passing not buying
                #subtract from price of index
                buy = dfs(i+1,not buying) - prices[i]
                #cooldown = dfs but with i + 1
                cooldown = dfs(i+1,buying)
                
                #cache result the max of buy and cooldown
                dp[(i,buying)] = max(buy,cooldown)
            else:
                #if we sell we increment by two negate boolean
                #add price of index
                sell = dfs(i+2,not buying) + prices[i]
                #cooldown = dfs but with i + 1
                cooldown = dfs(i+1,buying)
                #cache result the max of sell and cooldown
                dp[(i,buying)] = max(sell,cooldown)

            return dp[(i,buying)]
        return dfs(0,True)


        