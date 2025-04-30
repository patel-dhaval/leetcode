class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        max_area = 0

        def dfs(r, c):
            
            visit.add((r,c))
            directions = [[1,0], [-1, 0], [0,1 ], [0, -1]]
            area = 1
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visit or grid[row][col] == 0:
                    continue
                  
                area += dfs(row, col)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    temp_a = dfs(r, c)
                    max_area = max(max_area, temp_a)
        
        return max_area
        