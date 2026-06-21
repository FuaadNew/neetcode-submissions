class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions =[[0,1],[1,0],[0,-1],[-1,0]]
        ROWS,COLS = len(grid),len(grid[0])
        q = deque([])
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if (r >= 0 and c >= 0 and r < ROWS and c < COLS and (r,c) not in visit
                    and grid[r][c] != -1):
                    visit.add((r,c))
                    grid[r][c] = distance

                    for dr,dc in directions:
                        newRow,newCol = r + dr, c + dc
                        q.append((newRow,newCol))
            distance+=1
