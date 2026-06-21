class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #create dictionary of lists
        edges = collections.defaultdict(list)

        #go through every edge(u,v,w) in the times input
        #map u to neighbor and weight
        for u,v,w in times:
            edges[u].append((v,w))
        
        #create minHeap with default values:
        minHeap = [(0,k)]
        #visit set
        visit = set()
        #result 
        t = 0
        #while minHeap
        while minHeap:
            #pop weight and node
            w1,n1 = heapq.heappop(minHeap)
            #check if in visit
            if n1 in visit:
                continue 
            #add to visit
            visit.add(n1)
            #update result to the max of itself and new weight
            t= max(t,w1)

            #go through neighbors and weight of this node and add to minHeap
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    #the weight getting to this node is also added
                    heapq.heappush(minHeap,(w2 + w1,n2))
        return t if len(visit) == n else -1


