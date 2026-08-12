class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board),len(board[0])
        board_count = {}
        word_count = {}
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for char in word:
            if char not in word_count:
                word_count[char] = 0
            word_count[char]+=1

        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                if char not in board_count:
                    board_count[char] = 0
                board_count[char]+=1
        
        for char in word_count:
            if char not in board_count or board_count[char] < word_count[char]:
                return False

        def solve(r,c):
        
            stack = [[r,c,set(),-1, 0, False]]
            NEI = 3
            INDEX = 4
            RESULT = 5
    
            while stack:
                r,c,visit, nei, i,val = stack[-1]
                if nei == -1:
                    if i == len(word):
                        stack[-2][RESULT] = stack[-2][RESULT] or True
                        stack.pop()
                    elif (r,c) in visit:
                        stack.pop()
                    elif r < 0 or r >= ROWS or c < 0 or c >= COLS:
                        stack.pop()
                    elif word[i] != board[r][c]:
                        stack.pop()
                    else:
                        visit.add((r,c))
                        stack[-1][NEI] = 0
                elif nei < 4:
                    dr,dc = directions[nei]
                    nr, nc = r + dr, c + dc
                    stack[-1][NEI]+=1
                    stack.append([nr,nc,visit,-1, i + 1, False])
                else:
                    visit.remove((r,c))
                    stack.pop()
                    if not stack:
                        return val
                    stack[-1][RESULT] = stack[-1][RESULT] or val

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if solve(r,c):
                    return True
        return False
        
