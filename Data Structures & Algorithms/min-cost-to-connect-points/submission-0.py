class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i + 1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        #intialize a res array
        res = 0
        #initalize a visit set
        visit = set()
        #create a minHeap with cost and point
        minH = [[0,0]]
        #while visit set is less than N
        while len(visit) < N:
            #pop from minHeap cost and point i
            cost,i = heapq.heappop(minH)
            #if duplicate skip
            if i in visit:
                continue
            #add cost to result
            res+=cost
            #add to visit i
            visit.add(i)
            #go through every cost and neighbor of i in adjacency list
            for neiCost, nei in adj[i]:
                #if neighbor not in visit
                #add to minHeap the cost and nei
                if nei not in visit:
                    heapq.heappush(minH,[neiCost, nei])
        return res

            

        