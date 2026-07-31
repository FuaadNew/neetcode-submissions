class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * (numCourses)
        adj = {}

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            if b not in adj:
                adj[b] = []
            adj[b].append(a)
            indegrees[a]+=1
     
        q = deque([])
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
       
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            if curr not in adj:
                continue
            for nei in adj[curr]:
                indegrees[nei]-=1
                if indegrees[nei] == 0:
                    q.append(nei)
        if len(res) != numCourses:
            return []
        return res


        