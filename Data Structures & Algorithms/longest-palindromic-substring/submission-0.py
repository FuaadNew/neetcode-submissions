class Solution:
    def longestPalindrome(self, s: str) -> str:
        #declare result and reslen
        res = ""
        resLen = 0
        
        #longest length
        # go through every position in the string
        for i in range(len(s)):
            l,r = i,i
        #and consider them the center
        
        
            #odd length palindrome
            #left and right pointer set to i
            while l>=0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r +1]
                l-=1
                r+=1

            l,r = i,i+1
        #and consider them the center
        
        
            #odd length palindrome
            #left and right pointer set to i
            while l>=0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    res = s[l:r +1]
                l-=1
                r+=1
        return res
            