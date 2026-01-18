class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []

        visited_atl = set()
        visited_pac = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            
            visited.add((r,c))

            neighbours= [[1,0], [-1,0],[0,1],[0, -1]]

            for dr, dc in neighbours:
                row = r + dr
                col = c + dc

                if min(row, col) < 0 or row == ROWS or col == COLS or heights[r][c] > heights[row][col]:
                    continue
                dfs(row, col, visited)
        

        for r in [0]:
            for c in range(COLS):
                dfs(r, c, visited_pac)
            
        for r in [ROWS - 1]:
            for c in range(COLS):
                dfs(r, c, visited_atl)
        
        for r in range(ROWS):
            for c in [0]:
                dfs(r, c, visited_pac)
        
        for r in range(ROWS):
            for c in [COLS - 1]:
                dfs(r, c, visited_atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c ) in visited_atl and (r,c ) in visited_pac:
                    res.append([r,c])
        
        return res
