class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS,COLS = len(board), len(board[0])
        visit = set()
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O' or (r,c) in visit:
                return
            visit.add((r,c))
            board[r][c] = "G"
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        for c in range(COLS):
            if board[0][c] == "O" and (0,c) not in visit:
                dfs(0,c)
            if board[ROWS-1][c] == "O" and (ROWS-1, c) not in visit:
                dfs(ROWS-1,c)

        for r in range(ROWS):
            if board[r][0] == "O" and (r,0) not in visit:
                dfs(r,0)
            if board[r][COLS-1] == "O" and (r,COLS-1) not in visit:
                dfs(r,COLS-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "G":
                    board[r][c] = "O"
        
        
        
            


        