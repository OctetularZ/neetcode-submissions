class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top_row, bottom_row = 0, rows - 1

        search_row = -1

        while top_row <= bottom_row:
            mid = (top_row + bottom_row) // 2

            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                search_row = mid
                break
            
            if matrix[mid][cols - 1] < target:
                top_row = mid + 1
            elif matrix[mid][0] > target:
                bottom_row = mid - 1
        
        if search_row == -1:
            return False
        
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[search_row][mid] == target:
                return True
            
            if matrix[search_row][mid] < target:
                left = mid + 1
            elif matrix[search_row][mid] > target:
                right = mid - 1
        
        return False