class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #initialize our q
        q = deque()
        #initialize time and how many fresh oranges exist at given time

        time,fresh = 0,0
        ROWS, COLS = len(grid),len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh >0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append([nr,nc])
            time+=1
        return time if fresh == 0 else -1
        
        #get dimenstions of grid
        
        #iterate through entire grid for preword
        
                #count number of fresh oranges
                
                #identify rotten oranges to add to queue
                
        
        #while q is not empty and there are still fresh oranges
        
            #iterate through queue to pop rotten oranges
            
                #adding adjacent elements to the queue 
                #pop from q and add adjacent
                
                #for dr and dc in dirctions
                
                    #nr,nc
                    
                    # if r and c not in range or not fresh continue
                    
                    #make that position rotten and add to queue
                    
                    #decrement fresh oranges
                    
            #after for loop if done iterating increment time
            
        #return time if fresh == 0
        
                    
        





