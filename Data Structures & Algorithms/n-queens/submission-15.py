class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(r,c, board):
            #go right as possible            
            for nc in range(c + 1, n):
                if board[r][nc] == "Q":
                    return False
            #go left as possible            
            for nc in range(c - 1, - 1, -1):
                if board[r][nc] == "Q":
                    return False
            
            #go up as possible            
            for nr in range(r - 1, - 1, -1):
                if board[nr][c] == "Q":
                    return False
            
            #go up-right diagnol as far as possible
            i,j = r - 1,c + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i-=1
                j+=1
            
            #go up-left diagnol as far as possible
            i,j = r - 1,c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1

            return True
             

        res = []
        def dfs(r, board):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                board[r][c] = "Q"
                if valid(r,c, board):
                    dfs(r + 1, board)
                board[r][c] = "."
        
        board = [['.'] * n for _ in range(n)]
        dfs(0, board)
        return res