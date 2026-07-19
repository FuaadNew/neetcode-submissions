class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque([])
        visit = set()
        ROWS,COLS = len(grid),len(grid[0])
        islands = 0
        def bfs(r,c):
            q.append((r,c))
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    nr,nc = row + dr, col + dc
                    if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr,nc) not in visit
                    and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visit.add((nr,nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    if (r,c) not in visit:
                        islands+=1
                        bfs(r,c)
        return islands



            