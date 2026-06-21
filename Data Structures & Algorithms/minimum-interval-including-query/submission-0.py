class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #sort our intervals
        intervals.sort()
        #create MinHeap 
        minHeap = []
        #result hashmap, and index parameters
        res,i = {},0
        #sort the queries array in the forloop
        for q in sorted(queries):
            #iterate through intervals 
            #add intervals to minHeap while left value of
            # interval is less than or equal to our query value
            while i< len(intervals) and intervals[i][0] <= q:
                # get left and right value from interval
                l,r = intervals[i]
                #push onto Heap the size of the interval 
                #and the tie breaker value (right)
                heapq.heappush(minHeap,(r-l + 1,r))
                #increment i
                i+=1
            #pop from minHeap if interval is too right and minHeap if not empty
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            #grab smallest length from minHeap if exist otherwise -1 and add to res hashmap
            res[q] = minHeap[0][0] if minHeap else -1
            
        #return result in original order
        return [res[q] for q in queries]
        
             

