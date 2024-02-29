class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Optimal Solution
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1
        # step 1: Traverse the matrix and
        # mark 1st row & col accordingly:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark i-th row:
                    matrix[i][0] = 0

                    # mark j-th column:
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    # check for col & row:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0

        #step 3: Finally mark the 1st col & then 1st row:
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        # # with extra memory
        # row_header = [0] * len(matrix) 
        # column_header = [0] * len(matrix[0])
        
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[row])):
        #        if matrix[row][col] == 0:
        #             row_header[row] = 1
        #             column_header[col] = 1


        # for row in range(len(matrix)):
        #     for col in range(len(matrix[row])):
        #         if row_header[row] or column_header[col]:
        #             matrix[row][col] = 0

        