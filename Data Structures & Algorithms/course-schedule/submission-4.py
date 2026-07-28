class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if crs not in adj:
                return True
            if adj[crs] == []:
                return True
            visit.add(crs)

            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            adj[crs] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True