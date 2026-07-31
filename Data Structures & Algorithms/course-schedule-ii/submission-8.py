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
            stack = [[i,-1]]

            while stack:
                curr,next_index = stack[-1]

                if next_index == -1:
                    if curr in visit:
                        return False
                    if curr in completed:
                        stack.pop()
                        continue
                    if curr not in adj:
                        res.append(curr)
                        completed.add(curr)
                        stack.pop()
                        continue
                    visit.add(curr)
                    stack[-1][1] = 0
                next_index = stack[-1][1]
                neighbors = adj.get(curr, [])
                if 0<= next_index < len(neighbors):
                    stack[-1][1]+=1
                    nei = neighbors[next_index]
                    stack.append([nei,-1])
                else:
                    visit.remove(curr)
                    completed.add(curr)
                    stack.pop()
                    res.append(curr)

            return True


        for i in range(numCourses):
            if not solve(i):
                return []
        return res