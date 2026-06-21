class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        res =0
        heapq.heapify(min_heap)
        for num in nums:
            heapq.heappush(min_heap,-num)
        while k > 0:
            res = heapq.heappop(min_heap)
            k-=1
        return (-res)
