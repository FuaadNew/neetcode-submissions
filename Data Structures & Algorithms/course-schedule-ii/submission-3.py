class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        for i in range(len(prerequisites)):
            a,b = prerequisites[i]
            adj[a].append(b)
        visit = set()
        completed = set()
        res = []
        def dfs(i):
            if i in completed:
                return True
            if i in visit:
                return False
            if i not in adj:
                completed.add(i) 
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