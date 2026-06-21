class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False

        for char in range(len(s)):
            sDict[s[char]] = 1 + sDict.get(s[char],0)
            tDict[t[char]] = 1 + tDict.get(t[char],0)
        return sDict == tDict

        