class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def dfs(open_count, close_count, path):
            if open_count == close_count == n:
                res.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                dfs(open_count + 1, close_count, path)
                path.pop()
            if close_count < open_count:
                path.append(")")
                dfs(open_count, close_count + 1, path)
                path.pop()
        res = []
        dfs(0,0,[])
        return res
