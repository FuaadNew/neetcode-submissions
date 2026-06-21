class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visit = set()
        adj = defaultdict(list)
        
        for i in range(len(edges)):
            a,b = edges[i]
            adj[a].append(b)
            adj[b].append(a)


        def dfs(node,parent):
            if node in visit:
                return 
            if adj[node] == []:
                return 
            
            visit.add(node)

            for nei in adj[node]:
                if nei == node:
                    continue
                dfs(nei,node)
        
        for i in range(n):
            if i not in visit:
                res+=1
                dfs(i,-1)
        return res


            

       