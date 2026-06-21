class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS,COLS = len(matrix),len(matrix[0])
        def set_row(row):
            for c in range(len(matrix[0])):
                if matrix[row][c] != 0:
                    matrix[row][c] = 'X'
        
        def set_col(col):
            for r in range(len(matrix)):
                if matrix[r][col] != 0:
                    matrix[r][col] = 'X'
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    set_row(r)
                    set_col(c)

    
        print(matrix)


        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 'X':
                    matrix[r][c] = 0
        

        