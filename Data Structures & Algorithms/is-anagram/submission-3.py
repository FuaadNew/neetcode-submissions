class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        if len(s) != len(t):
            return False
        for i in range (len(s)):
            sdict[s[i]] = 1 + sdict.get(s[i],0)
            tdict[t[i]] = 1 + tdict.get(t[i],0)
        return sdict == tdict


        
        