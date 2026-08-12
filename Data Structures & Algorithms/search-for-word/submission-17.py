class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board),len(board[0])

        def dfs(r,c,i,visit):
            if i == len(word):
                return True
            if (r,c) in visit:
                return False
            if r < 0 or r>= ROWS or c < 0 or c >=COLS:
                return False
            if word[i] != board[r][c]:
                return False

            visit.add((r,c))

            left = dfs(r,c - 1,i + 1, visit)
            right = dfs(r,c + 1,i + 1, visit)
            up = dfs(r - 1,c,i + 1, visit)
            down = dfs(r + 1,c,i + 1, visit)
            res = left or right or up or down
            visit.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0,set()):
                    return True
        return False