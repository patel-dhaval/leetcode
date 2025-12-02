class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while len(res) < (len(matrix)* len(matrix[0])): 
            # left to right
            for col in range(left, right+1):
                res.append(matrix[up][col])

            up+=1

            # down

            for row in range(up, down+1):
                res.append(matrix[row][right])

            right -= 1

            # right to left

            if up <= down:
                for col in range(right, left-1, -1):
                    res.append(matrix[down][col])
                
                down -= 1

            # down to up
            if left <= right:
                for row in range(down, up-1, -1):
                    res.append(matrix[row][left])
                
                left += 1

        return res

        
        