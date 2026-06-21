class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        adj = defaultdict(list)

        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        print(adj.items())
        
        visit = set()
        #no cycle 
        def dfs(node,parent):
            if node in visit:
                return False
            
            if adj[node] == []:
                return True
            
            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei,node):
                    return False
            
            adj[node] = []
            return True




        #all nodes are connected
        
        return dfs(0,-1) and len(visit) == n
