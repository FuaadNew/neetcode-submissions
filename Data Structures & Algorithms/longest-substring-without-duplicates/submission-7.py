class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        maxLength = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            hashSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength