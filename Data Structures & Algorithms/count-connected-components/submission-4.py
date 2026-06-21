class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visit = set()

        adj = defaultdict(list)

        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)

            for nei in adj[node]:
                if nei == node:
                    continue
                dfs(nei)
        
        for i in range(n):
            if i not in visit:
                res+=1
                dfs(i)
        return res
                
