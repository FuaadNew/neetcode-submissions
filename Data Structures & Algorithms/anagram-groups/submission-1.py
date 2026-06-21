class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            s_sorted = sorted(s)
            key = tuple(s_sorted)

            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)
        return ans.values()
      
        