class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix)-1
        while top<=bottom:
            row = (top + bottom) //2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        curr_row = matrix[row]
        l,r = 0,len(curr_row)-1
        while l<=r:
            mid = (l + r) //2
            if curr_row[mid] == target:
                return True
            if curr_row[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return False 