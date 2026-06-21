class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                second = first - second
                heapq.heappush(stones,second)
        if stones:
            return abs(stones[0])
        else:
            return 0






        