class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sort by frequency
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num,0) + 1
        sorted_freqs = sorted(freq_map.items(), key = lambda x: x[1])
        res = []
        while k:
            key, val = sorted_freqs.pop()
            res.append(key)
            k-=1
        return res