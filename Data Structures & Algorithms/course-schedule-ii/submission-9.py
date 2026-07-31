class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            if a not in adj:
                adj[a] = []
            adj[a].append(b)

        visit = set()
        completed = set()
        res = []

        def solve(i):
            stack = [[i,False]]

            while stack:
                curr,returning = stack[-1]
                if returning:
                    visit.remove(curr)
                    completed.add(curr)
                    res.append(curr)
                    stack.pop()
                else:
                    if curr in visit:
                        return False
                    if curr in completed:
                        stack.pop()
                        continue
                    if curr not in adj:
                        completed.add(curr)
                        res.append(curr)
                        stack.pop()
                        continue
                    visit.add(curr)
                    stack[-1][1] = True
                    for nei in adj[curr]:
                        stack.append([nei, False])
            return True


        for i in range(numCourses):
            if not solve(i):
                return []
        return res