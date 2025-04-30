class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(r, c):
            
            visit.add((r,c))
            directions = [[1,0], [-1, 0], [0,1 ], [0, -1]]
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visit or grid[row][col] == '0':
                    continue
                  
                dfs(row, col)

        count = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(r, c)
                    count += 1
        
        return count
        
