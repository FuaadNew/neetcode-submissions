class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        cols = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
                

            for c in range(n):
                if (r + c) in posDiag or (r - c) in negDiag or c in cols:
                    continue
            
                posDiag.add(r+c)
                negDiag.add(r-c)
                cols.add(c)
                board[r][c] = "Q"
                dfs(r+1)

                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cols.remove(c)
                board[r][c] = "."

        dfs(0)
        return res
        