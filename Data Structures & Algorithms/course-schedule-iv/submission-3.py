class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        
        for a,b in prerequisites:
            adj[a].append(b)


        from functools import cache
        @cache
        def find(source, dest):
            if source == dest:
                return True
            
            for nei in adj[source]:
                if find(nei, dest):
                    return True
            return False
        res =[]
        cache = {}
        for a,b in queries:
            result = find(a,b)
            cache[(a,b)] = True
            res.append(find(a,b))
        return res

