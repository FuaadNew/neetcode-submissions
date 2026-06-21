class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #get length of grid for visit comparison
        N = len(grid)
        #get visit set
        visit = set()
        #minHeap with default values of topleft corner and r,c
        minHeap =[[grid[0][0],0,0]]
        #directions array for four directions 
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        #add to visit set the top left corner
        visit.add((0,0))
        #while minHeap is not empty
        while minHeap:
            #pop from minHeap the time and row/column 
            t,r,c = heapq.heappop(minHeap)
            #if this position is the destionation (the bottom right spot)
            if r == N -1 and c == N -1:
                #return the time it took to get here
                return t
            #if not traverse the four neighbors
            #go through dr,dc in directions
            for dr,dc in directions:
                neiR,neiC = r+dr, c + dc
                #check if out of bounds or in visit skip
                if (neiR < 0  or neiC < 0 or neiR == N or neiC == N or (neiR,neiC) in visit):
                    continue
                #add to visit 
                visit.add((r,c))
                #max of position and t, nr,nc
                heapq.heappush(minHeap, [max(t,grid[neiR][neiC]),neiR,neiC])
        
                



            
        