class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visit = set()
        adj = defaultdict(list)
        
        for i in range(len(edges)):
            a,b = edges[i]
            adj[a].append(b)
            adj[b].append(a)


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


            

       