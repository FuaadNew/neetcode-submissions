class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0, len(matrix)-1
        while top<=bottom:
            row = (top + bottom) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        current_row = matrix[row]
        l,r = 0, len(current_row)-1

        while l<=r:
            mid = (l + r)//2
            if current_row[mid] == target:
                return True
            if current_row[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return False