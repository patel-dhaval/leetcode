class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0        
        
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        def dfs(r, c):
            visit.add((r,c))
            area = 1
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (min(row, col) < 0 
                    or row == ROWS 
                    or col == COLS 
                    or grid[row][col] == 0
                    or (row,col) in visit):
                    continue
                area += dfs(row, col)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 1:
                    current_area = dfs(r, c)
                    print(current_area)
                    if current_area > max_area:
                        max_area = current_area

        return max_area