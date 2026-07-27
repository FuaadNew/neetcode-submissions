class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        completed = set()
      

        for a,b in prerequisites:
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
        
        #print(adj.items())

        def dfs(crs, visit):
            if crs in completed:
                return True
            if crs in visit:
                return False
            if crs not in adj:
                return True
            visit.add(crs)
         
            for nei in adj[crs]:
                if not dfs(nei, visit):
                    return False
            visit.remove(crs)
            completed.add(crs)
            return True
            
      

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True