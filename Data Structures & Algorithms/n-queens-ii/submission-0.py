class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        def valid(r,c, board):
            #go right
            for nc in range(c + 1, n):
                if board[r][nc] == "Q":
                    return False
            #go left
            for nc in range(c - 1, -1,  -1):
                if board[r][nc] == "Q":
                    return False


            #go up
            for nr in range(r - 1, -1,  -1):
                if board[nr][c] == "Q":
                    return False

            i,j = r - 1, c + 1
            #go up-right diagnol

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i-=1
                j+=1

            i,j = r - 1, c - 1
            #go up-left diagnol
            while i >= 0 and j >=0:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1
            return True

        def dfs(r, board, total):
            if r == n:
                return 1
            res = 0
            for c in range(n):
                if valid(r,c, board):
                    board[r][c] = "Q"
                    res+= dfs(r + 1, board, total)
                    board[r][c] = "."
            return res 


        board = [['.'] * n for _ in range(n)]
        return dfs(0, board,0)
