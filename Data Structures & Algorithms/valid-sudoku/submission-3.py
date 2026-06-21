class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS,COLS = len(board),len(board[0])
        squares = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    print(board[r][c])
                    print(rows[r])
                    print("row hit")
                    return False
                
                if board[r][c] in cols[c]:
                    print("col hit")
                    return False

                if board[r][c] in squares[(r//3,c//3)]:
                    print("square hit")
                    return False
                rows[r].add(board[r][c])    
                cols[c].add(board[r][c])    
                squares[(r//3,c//3)].add(board[r][c])  
        return True              


