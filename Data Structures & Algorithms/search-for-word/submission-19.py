class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board),len(board[0])
        directions = [(0,1), (1,0),(0,-1),(-1,0)]
        counter = defaultdict(int)
        for r in range(ROWS):
            for c in range(COLS):
                counter[board[r][c]]+=1
        wordCount = Counter(word)
        for c in wordCount:
            if c not in counter or  counter[c] < wordCount[c]:
                return False

        def solve(r,c):
            #row column, curIndex, visit set, return Value, index
            stack = [[r,c,-1, set(), False, 0]]
            CUR_INDEX = 2
            RETURN = 4
            index = 5

            while stack:
                r,c,cur_index, visit, val, i = stack[-1]
                if cur_index == -1:
                    if i == len(word):
                        stack[-2][RETURN] = stack[-2][RETURN] or True
                        stack.pop()
                    elif (r,c) in visit:
                        stack.pop()
                    elif r < 0 or r >= ROWS or c < 0 or c >= COLS:
                        stack.pop()
                    elif word[i] != board[r][c]:
                        stack.pop()
                    else:

                        stack[-1][CUR_INDEX] = 0
                        visit.add((r,c))
                elif stack[-1][CUR_INDEX] <4:
                    dr,dc = directions[cur_index]
                    nr,nc = r + dr, c + dc
                    stack[-1][CUR_INDEX]+=1
                    stack.append([nr,nc, -1, visit, False, i + 1])
                else:
                    visit.remove((r,c))
                    stack.pop()
                    if not stack:
                        return val
                    stack[-1][RETURN] = stack[-1][RETURN] or val
                    
                    
                    




        for r in range(ROWS):
            for c in range(COLS):
                if solve(r,c):
                    return True
        return False