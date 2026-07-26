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
        
        def solve(src, target):
            stack = [(src, 1)]
            visit = set()
            while stack:
                curr,w = stack.pop()
                print(curr,target,w)
                if curr == target:
                    return w
                if curr not in adj:
                    continue
                if curr in visit:
                    continue
                visit.add(curr)
                for nei,weight in adj[curr]:
                    stack.append((nei, w * weight))
            return -1
        res = [0] * len(queries)
        for i in range(len(queries)):
            a,b = queries[i]
            if a not in adj or b not in adj:
                res[i]= -1.0
            else:
                res[i]= solve(a,b)
        return res

            
        