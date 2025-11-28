class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_set = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c):            
            neighbours = [[0, 1], [0,-1], [1, 0], [-1, 0]]

            for dr, dc in neighbours:
                row = r+dr
                col = c + dc
                if min(row, col) < 0 or row == ROWS or col == COLS or grid[row][col] == '0' or (row, col) in visited_set:
                    continue
                visited_set.add((row,col))
                dfs(row, col)
            
            return

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited_set:
                    dfs(r,c)
                    count += 1
        
        return count