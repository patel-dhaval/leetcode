class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image

        visited = set()

        def dfs(r,c):
            
            visited.add((r,c))
            image[r][c] = color
            directions = [[0,1], [0, -1], [1,0], [-1, 0]]

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if row < rows and col < cols and row >= 0 and col >= 0 and (row, col) not in visited and image[row][col] == original_color:
                    dfs(row, col)
            
        
        dfs(sr, sc)

        return image
                
            