class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        buckets = [[] for _ in range(max(freq_map.values()) + 1)]
       

        for key,val in freq_map.items():
            buckets[val].append(key)

        res = []
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
            
