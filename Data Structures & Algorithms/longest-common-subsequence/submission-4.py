class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #set dp column of arrays of all 0 of length text2 + 1
        #set dp row for length text 1 + 1
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1) ]

        #nested loop iterate through 2-d Array in reverse order
        #for both i and j
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                #if the characters in both strings i/j match 
                if text1[i] == text2[j]:
                    #dp at [i][j] = 1 + diagnal
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    #if they don't match it'll be the maximum of the values to the top/below
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        
        #return result at topleft
        return dp[0][0]