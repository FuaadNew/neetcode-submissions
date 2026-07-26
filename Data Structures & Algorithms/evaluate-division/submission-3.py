class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}

        for i in range(len(equations)):
            a,b = equations[i]
            value = values[i]
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            
            adj[a].append((b,value))
            adj[b].append((a,1/value))
        print(adj.items())
        
        def dfs(curr, w, target, visit):
            if curr == target:
                return w
            if curr not in adj:
                return -1.0
            visit.add(curr)
            for nei, weight in adj[curr]:
                if nei in visit:
                    continue
                result = dfs(nei, w * weight, target, visit)
                if result != -1.0:
                    return result
            return -1.0            


        res = [0] * len(queries)
        for i in range(len(queries)):
            a,b = queries[i]
            if a not in adj or b not in adj:
                res[i]= -1.0
            else:
                res[i]= dfs(a,1, b, set())
        return res

            
        