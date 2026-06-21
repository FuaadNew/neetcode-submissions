class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #make bottom row full of 1
        row =[1]* n
        #go through all rows except last one
        for i in range(m-1):
            #for each row compute newRow
            #one above the old row
            newRow = [1] * n
            #go through every column except the last one in reverse order
            for j in range(n-2,-1,-1):
                #newRow[j] is the row at j + 1 plus row[j]
                newRow[j] = newRow[j+1] + row[j]
            #row = newRow
            row = newRow
        #return value at row[0]
        return row[0]



        