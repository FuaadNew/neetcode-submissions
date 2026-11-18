class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            self.max_heap.append(-num)
            return

        if num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        #rebalancing
        #self.max_heap has one extra element allowed
        if len(self.min_heap) > len(self.max_heap):
            candidate = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -candidate)
            
        elif len(self.max_heap) > len(self.min_heap) + 1:
            candidate = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, candidate)



         

    def findMedian(self) -> float:
        total_length = len(self.min_heap) + len(self.max_heap)

        if total_length % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()