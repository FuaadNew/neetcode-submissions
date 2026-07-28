class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
        visit = set()
        def solve(crs):
            stack = [(crs, False)]
            while stack:
                curr, returning = stack.pop()
                if returning:
                    visit.remove(curr)
                    adj[curr] = []
                else:
                    if curr in visit:
                        return False
                    if curr not in adj:
                        continue
                    if adj[curr] == []:
                        continue
                    visit.add(curr)
                    stack.append((curr,True))
                    for nei in adj[curr]:
                        stack.append((nei, False))
            return True
        
        for i in range(numCourses):
            if not solve(i):
                return False
        return True