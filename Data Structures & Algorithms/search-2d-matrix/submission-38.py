class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #binary search which row 
        l,r = 0, len(matrix)-1

        while l<=r:
            row = (l + r )// 2

            last_val = matrix[row][-1]
            first_val = matrix[row][0]

            if target > last_val:
                l = row + 1
            elif target < first_val:
                r = row - 1
            else:
                break
        
        row = matrix[row]
        l,r = 0, len(row)-1

        while l<=r:
            mid = (l + r) // 2

            if row[mid] == target:
                return True
            if row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False