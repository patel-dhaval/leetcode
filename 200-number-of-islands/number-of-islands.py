class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [[1,0], [-1, 0], [0,1], [0,-1]]
        visited = set()
        island_count = 0

        def dfs(r,c):
            if (r,c) in visited:
                return

            visited.add((r,c))

            for dr, dc in neighbours:
                row = r + dr
                col = c + dc

                if min(row,col) < 0 or row == ROWS or col == COLS or (row, col) in visited or grid[row][col] == '0':
                    continue
                dfs(row,col)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    island_count += 1
        
        return island_count
