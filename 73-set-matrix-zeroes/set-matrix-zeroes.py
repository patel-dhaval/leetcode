class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_header = [0] * len(matrix) 
        column_header = [0] * len(matrix[0])
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
               if matrix[row][col] == 0:
                    row_header[row] = 1
                    column_header[col] = 1


        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row_header[row] or column_header[col]:
                    matrix[row][col] = 0

        
        # print(row_header)
        # print(column_header)        
        # print(matrix)
                              