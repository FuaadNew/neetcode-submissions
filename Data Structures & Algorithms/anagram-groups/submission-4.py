class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        for string in strs:
            key = sorted(string.lower())
            hashKey = tuple(key)
            if hashKey in anaDict:
                anaDict[hashKey].append(string)
            else:
                anaDict[hashKey] = [string]
        return anaDict.values()
        