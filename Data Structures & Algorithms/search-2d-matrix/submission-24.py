class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top,bottom = 0,len(matrix)-1
        while top<=bottom:
            curRow = (top + bottom)//2
            if matrix[curRow][-1] < target:
                top = curRow + 1 
                
            elif matrix[curRow][0] > target:
                bottom = curRow - 1 

            else:
                break

        l,r = 0, len(matrix[curRow])-1
        while l<=r:
            mid = (l + r) //2
            if matrix[curRow][mid] == target:
                return True
            if matrix[curRow][mid] < target:
                l = mid + 1
            else:
                r = mid -1
        
        return False
            

        