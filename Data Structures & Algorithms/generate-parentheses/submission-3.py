class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(complete_count,open_count, path):
            if complete_count == n:
                res.append("".join(path))
                return
            #choose an open
            #open choice is available if openCount is less than n
            if open_count < n:
                path.append("(")
                dfs(complete_count,open_count + 1, path)
                path.pop()
            #choose a close
            #if we choose a close then inrement complete count
            if open_count > complete_count:
                path.append(")")
                dfs(complete_count + 1,open_count, path)
                path.pop()
      
        dfs(0, 0, [])
        return res
