class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        hashSet = set()
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            res = max(res,r-l+1)
            hashSet.add(s[r])
        return res
        