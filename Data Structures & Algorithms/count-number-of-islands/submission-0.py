class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #check if we have a grid 
        # if not return 0
        if not grid:
            return 0
        
        # get dimensions of grid
        rows = len(grid)
        cols = len(grid[0])
        #create set to mark cells as visited 
        visit = set()
        #var to count number of islands
        islands = 0
        #iterate through every row and cols

        #def bfs

        def bfs(r,c):
            #queue to store iteratively
            q = deque()
            #mark spot as visited 
            visit.add((r,c))
            #append to queue as ((r,c))
            q.append((r,c))

            #while q is not empty
            while q:
                #we will expand our island
                #pop from the queue
                row,col = q.popleft()
                #check adjacent positions 
                #loop through directions 
                directions = [[1,0], [-1,0], [0,1],[0,-1]]
                #for each of these dr,dc in directions 
                for dr,dc in directions:
                    #if r + dr or c + dc in range(rows or cols)
                    r,c = row + dr, col + dc
                    #and if grid[r + dr][c + dc] is 1
                    #and position not in visit
                    if ((r) in range(rows) and (c) in range(cols) and grid[r][c] == "1"
                    and(r,c) not in visit):
                    #we need to add this position to the queue 
                    #we need to mark it as visited
                        q.append((r,c))
                        visit.add((r,c))
            


        for r in range(rows):
            for c in range(cols):
                #if we visit a 1 and that 1 is not in viist
                if grid[r][c] == "1" and (r,c) not in visit:
                    #call bfs
                    bfs(r,c)
                    #increment number of islands
                    islands+=1
        #return number of islands
        return islands

