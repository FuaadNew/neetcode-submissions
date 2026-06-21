class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        longestSubString = 0
        l, r = 0, 0
        
        while r < len(s):
            while s[r] in hashSet:
                hashSet.remove(s[l])  # Corrected the method call
                l += 1
            
            hashSet.add(s[r])
            longestSubString = max(longestSubString, r - l + 1)
            
            r += 1
        
        return longestSubString