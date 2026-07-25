class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = {}
        for i in range(len(equations)):
            a,b = equations[i]
            weight = values[i]
            if a not in adj_list:
                adj_list[a] = []
            if b not in adj_list:
                adj_list[b] = []
            adj_list[a].append((b, weight))
            adj_list[b].append((a, 1/weight))


        
        def solve(a,b):
            stack = []
            stack.append((a, 1))
            visit = set()
            while stack:
                curr,curWeight = stack.pop()
                if curr == b:
                    return curWeight
                if curr in visit:
                    continue
                visit.add(curr)
                if curr not in adj_list:
                    continue
                for nei,weight in adj_list[curr]:
                    stack.append((nei, weight *curWeight))
            return -1.0

        res = []
        for a,b in queries:
            if a not in adj_list:
                res.append(-1.0)
            else:
                res.append(solve(a,b))
        return res
            
        