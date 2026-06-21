class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        t =0
        visit = set()
        for u,v,w in times:
            edges[u].append((v,w))
        minHeap = [(0,k)]
        while minHeap:
            w1,v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue
            visit.add(v1)
            t = max(t,w1)
            for v2,w2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap,(w2 + w1,v2))
        return t if len(visit) == n else -1

            
        
        