"""
Approach:
Lets convert the 2d input into a flat input, since we know the ip conditions, flattening is feasible.
Identifying row and column would be the tricky bit.
We can use division and modulo operators
Div will help identify how many complete rows would fit, and the modulo operator will help find the exact location in the partial row.

Eg:

If we get middle value as 6
Coordinates would be 6//4 and 6%4 -> 1, 2, thats 11
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        R = (rows * cols) - 1

        while L <= R:
            mid = (L + R)//2
            if target > matrix[mid//cols][mid%cols]:
                L = mid + 1
            elif target < matrix[mid//cols][mid%cols]:
                R = mid - 1
            else:
                return True
        
        return False