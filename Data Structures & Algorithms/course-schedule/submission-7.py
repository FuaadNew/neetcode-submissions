class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adj = {}

        for a,b in prerequisites:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
            indegrees[b]+=1

        q = deque([])
        print(indegrees)
        res = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
      
        while q:
            curr = q.popleft()
            res.append(curr)
            if curr not in adj:
                continue
            for nei in adj[curr]:
                indegrees[nei]-=1
                if indegrees[nei] == 0:
                    q.append(nei)
        return len(res) == numCourses
