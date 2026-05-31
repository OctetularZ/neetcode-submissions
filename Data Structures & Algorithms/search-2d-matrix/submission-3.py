class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows - 1

        while left <= right:
            mid = (left + right) // 2
            smallest = matrix[mid][0]
            largest = matrix[mid][cols - 1]

            if smallest <= target <= largest:
                inner_left, inner_right = 0, cols - 1
                while inner_left <= inner_right:
                    inner_mid = (inner_left + inner_right) // 2
                    search = matrix[mid][inner_mid]
                    if search == target:
                        return True
                    
                    if search < target:
                        inner_left = inner_mid + 1
                    else:
                        inner_right = inner_mid - 1
                return False
            else:
                if target > largest:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False

