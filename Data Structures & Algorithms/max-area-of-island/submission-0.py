class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        max_area = 0
        rows,cols = len(grid),len(grid[0])


        def bfs(r,c):
            area =1
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr,dc in directions:
                    nr,nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visit):
                        q.append((nr,nc))
                        visit.add((nr,nc))
                        area+=1
            return area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:    
                    max_area=max(max_area,bfs(r,c))
        return max_area
        