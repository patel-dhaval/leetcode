class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        perimeter = 0

        def dfs(r, c, visit):
            nonlocal perimeter
            visit.add((r,c))
            directions = [[1,0], [-1, 0], [0,1 ], [0, -1]]
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if min(row, col) < 0 or row == ROWS or col == COLS or grid[row][col] == 0:
                    perimeter += 1
                    continue
                
                if (row, col) in visit:
                    continue
                
                dfs(row, col, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c, set())
                    return perimeter

        # Array Manipulation
            
        # rows = len(grid)
        # cols = len(grid[0])
        # perimeter = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             perimeter += 4
        #             if r > 0 and grid[r-1][c] == 1:  
        #                 perimeter -= 2
        #             if c > 0 and grid[r][c-1] == 1:  
        #                 perimeter -= 2

        # return perimeter
