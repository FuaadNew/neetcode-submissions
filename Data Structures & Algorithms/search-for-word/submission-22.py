class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board),len(board[0])
        directions =[(0,1), (1,0),(0,-1), (-1,0)]
        wordCount = Counter(word)
        boardCount = defaultdict(int)
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                boardCount[char]+=1
        for c in wordCount:
            if c not in boardCount or boardCount[c]< wordCount[c]:
                return False
        def solve(r,c):
            NEI = 3
            INDEX = 4
            VAL = 5
            frame = [r,c, set(),-1, 0, False]
            stack = [frame]

            while stack:
                r,c,visit, nei, i, val = stack[-1]
                if nei == -1:
                    if i == len(word):
                        stack[-2][VAL] = True
                        stack.pop()
                    elif (r,c) in visit:
                        stack.pop()
                    elif r < 0 or r >=ROWS or c < 0 or c>= COLS:
                        stack.pop()
                    elif word[i] != board[r][c]:
                        stack.pop()
                    else:
                        visit.add((r,c))
                        stack[-1][NEI] = 0
                elif nei < 4:
                    dr,dc = directions[nei]
                    stack[-1][NEI]+=1
                    nr,nc = r + dr, c + dc
                    frame = [nr,nc, visit,-1, i + 1, False]
                    stack.append(frame)
                else:
                    stack.pop()
                    visit.remove((r,c))
                    if not stack:
                        return val
                    else:
                        stack[-1][VAL] = stack[-1][VAL] or val
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if solve(r,c):
                    return True
        return False

