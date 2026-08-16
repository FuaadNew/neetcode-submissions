class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        directions = [[-1,1, "up-right"],  [-1,-1, "up-left"], [-1,0, "up"]]
        def valid(r,c, board):
            for i in range(r - 1, -1, -1):
                if board[i][c] == "Q":
                    return False
            i,j = r -1, c -1

            while i >= 0 and j >=0:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1
            
            i,j = r -1, c + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i-=1
                j+=1
            return True



                    

        res = []
        def dfs(r,c, board):
            if r == n:
                res.append(["".join(row) for row in board[:]])
                return
            for nc in range(n):
                board[r][nc] = "Q"
                if valid(r,nc, board):
                    dfs(r + 1,nc, board)
                board[r][nc] = "."

        

        board = [["."] * n for _ in range(n)]
        dfs(0,0, board)
        return res
