class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
                
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        max_area = 0

        def dfs(r, c, area):
            
            if (r, c) in visit:
                return

            visit.add((r,c))
            neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            curr_area = 1
            for dr, dc in neighbours:
                row = r + dr
                col = c + dc

                if ( min(row, col) < 0 or row == ROWS or col == COLS  or (row, col) in visit or grid[row][col] == 0):
                    continue
                
                area += dfs(row, col, curr_area)
            return area

        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visit and grid[row][col] == 1:
                    area = dfs(row, col, 1)
                    max_area = max(max_area, area)
        
        return max_area
