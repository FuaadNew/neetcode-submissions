class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = {}
        for string in strs:
            key = tuple(sorted(string))
            if key in hashy:
                hashy[key].append(string)
            else:
                hashy[key] = [string]
        return hashy.values()
        