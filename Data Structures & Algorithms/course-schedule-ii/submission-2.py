class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
        
        completed = set()
        visit = set()
        res = []

        def solve(i):
            stack = [(i,False)]
            path = []

            while stack:
                curr, returning = stack.pop()
                if returning:
                    visit.remove(curr)
                    completed.add(curr)
                    path.append(curr)
                else:
                    if curr in visit:
                        return []
                    if curr in completed:
                        continue
                    if curr not in adj:
                        path.append(curr)
                        completed.add(curr)
                        continue
                    visit.add(curr)
                    stack.append((curr, True))

                    for nei in adj[curr]:
                        stack.append((nei, False))

            return path



        for i in range(numCourses):
            if i not in completed:
                temp_path = solve(i)
                if temp_path == []:
                    return []
                res.extend(temp_path)
       
        return res