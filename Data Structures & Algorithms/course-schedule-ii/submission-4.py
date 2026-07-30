class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        visit = set()
        completed = set()
        adj = {}
        res = []

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            if a not in adj:
                adj[a] = []
            adj[a].append(b)

        def dfs(i):
            if i in visit:
                return False
            if i in completed:
                return True
            if i not in adj and i not in completed:
                res.append(i)
                completed.add(i)
                return True
            visit.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visit.remove(i)
            completed.add(i)
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res