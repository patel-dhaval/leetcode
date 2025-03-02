class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid = heights
        ROWS, COLS = len(grid), len(grid[0])
        visited_pac = set()
        visited_atl = set()
        solution = []

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r,c))

            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                row = r+dr
                col = c+dc

                if min(row, col) < 0 or row == ROWS or col == COLS or (grid[r][c] > grid[row][col]):
                    continue
                dfs(row, col, visited)

        
        for c in range(COLS):
            dfs(0, c, visited_pac)
        
        for r in range(ROWS):
            dfs(r, 0, visited_pac)
        
        for c in range(COLS):
            dfs(ROWS-1, c, visited_atl)
    
        for r in range(ROWS):
            dfs(r, COLS-1, visited_atl)

        # print("PC", visited_pac)
        # print("ATL", visited_atl)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_atl and (r,c) in visited_pac:
                    solution.append([r,c])
        
        return solution