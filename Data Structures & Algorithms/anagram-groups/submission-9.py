class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')]+=1
            
            if tuple(count) not in hashMap:
                hashMap[tuple(count)] = []
            hashMap[tuple(count)].append(word)
        
        return list(hashMap.values())