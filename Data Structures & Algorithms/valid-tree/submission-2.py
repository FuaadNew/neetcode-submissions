class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for i in range(len(edges)):
            a,b = edges[i]
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        def dfs(node,parent):
            if node in visit:
                return False

            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
        
            
            return True

        if not dfs(0,-1):
            return False
        return len(visit) == n 
        


            