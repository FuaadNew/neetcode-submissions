class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS,COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            visit.add((r,c))
            directions =[[0,1],[1,0],[0,-1],[-1,0]]

            for dr,dc in directions:
                nr,nc = r + dr, c + dc
                if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr,nc) not in visit
                and grid[nr][nc] == "1"):
                    dfs(nr,nc)
            
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    if (r,c) not in visit:
                        islands+=1
                        dfs(r,c)
        return islands