class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        prev_row = [1]

        for i in range(1,rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1,len(row)-1):
                row[j] = prev_row[j-1] + prev_row[j]
            prev_row = row
        return prev_row
            



            

        

        