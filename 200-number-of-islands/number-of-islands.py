class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        count = 0

        def dfs(r, c):
            
            if (r, c) in visit:
                return

            visit.add((r,c))
            neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in neighbours:
                row = r + dr
                col = c + dc

                if ( min(row, col) < 0 or row == ROWS or col == COLS  or (row, col) in visit or grid[row][col] == '0'):
                    continue
                
                dfs(row, col)


        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visit and grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        
        return count


        