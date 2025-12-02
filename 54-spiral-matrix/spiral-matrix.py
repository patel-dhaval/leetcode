class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while len(res) < (len(matrix)* len(matrix[0])): 
            # left to right
            for i in range(left, right+1):
                res.append(matrix[up][i])

            up+=1

            # down

            for j in range(up, down+1):
                res.append(matrix[j][right])

            right -= 1

            # right to left

            if up <= down:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                
                down -= 1

            # down to up
            if left <= right:
                for j in range(down, up-1, -1):
                    res.append(matrix[j][left])
                
                left += 1

        return res

        
        