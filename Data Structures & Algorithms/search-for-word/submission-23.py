class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,i, visit):
            if i == len(word):
                return True
            if r >= ROWS or c >= COLS or r < 0 or c < 0:
                return False
            if (r,c) in visit:
                return False
            if board[r][c] != word[i]:
                return False
            visit.add((r,c))
            left = dfs(r, c - 1, i + 1, visit)
            right = dfs(r, c + 1, i + 1, visit)
            up = dfs(r - 1, c, i + 1, visit)
            down = dfs(r + 1, c, i + 1, visit)
            visit.remove((r,c))
            return left or right or up or down

        
        ROWS,COLS = len(board),len(board[0])
        word_count = Counter(word)
        board_count = defaultdict(int)
        for r in range(ROWS):
            for c in range(COLS):
                char = board[r][c]
                board_count[char]+=1
        for char in word_count:
            if char not in board_count or board_count[char] < word_count[char]:
                return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0, set()):
                    return True
        return False
            