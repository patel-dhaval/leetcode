class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # apply binary search:
        low = 0
        high = n * m - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // m # logic for 2D to 1D row
            col = mid % m #logic for 2D to 1D col
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False