class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')]+=1
            count = tuple(count)
            if count not in hash_map:
                hash_map[count] = []
            hash_map[count].append(word)
        return list(hash_map.values())

    