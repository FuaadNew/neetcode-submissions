class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            else:
                maxf = max(maxf, r-l + 1 )
        return maxf
                
        