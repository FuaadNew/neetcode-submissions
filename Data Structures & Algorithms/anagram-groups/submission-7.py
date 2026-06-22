class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            if tuple(sorted(word)) not in hash_map:
                hash_map[tuple(sorted(word))] = []
            hash_map[tuple(sorted(word))].append(word)

        return list(hash_map.values())