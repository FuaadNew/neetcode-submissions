class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for a,b in prerequisites:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)

        def solve(course):
            stack = [course]
            visit = set()
            while stack:
                curr = stack.pop()
                if curr not in adj:
                    continue
                if curr in visit:
                    continue
                visit.add(curr)
                for nei in adj[curr]:
                    if nei == course:
                        return False
                    stack.append(nei)

            return True
        print(adj.items())
        for i in range(numCourses):
            if not solve(i):
                print(i)
                return False
        return True