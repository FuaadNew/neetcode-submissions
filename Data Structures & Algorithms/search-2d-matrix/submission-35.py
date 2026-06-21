class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        while top<=bottom:
            row = (top + bottom)//2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
                
        
        
        l,r = 0, len(matrix[row])-1

        while l<=r:
            mid = (l + r) //2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid -1
            elif matrix[row][mid] < target:
                l = mid + 1
            
        return False

    
                 
        


        