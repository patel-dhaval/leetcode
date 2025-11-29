class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            visited_atl = set()
            visited_pac = set()
            ROWS = len(heights)
            COLS = len(heights[0])
            res = []
            def dfs_atl(r,c, visited_atl):            
                visited_atl.add((r,c))
                neighbours = [[0, 1], [0,-1], [1, 0], [-1, 0]]

                for dr, dc in neighbours:
                    row = r+dr
                    col = c + dc
                    if min(row, col) < 0 or row == ROWS or col == COLS or heights[row][col] < heights[r][c]  or (row, col) in visited_atl:
                        continue

                    dfs_atl(row, col, visited_atl)
                
                return
            
            def dfs_pac(r,c, visited_pac):            
                visited_pac.add((r,c))
                neighbours = [[0, 1], [0,-1], [1, 0], [-1, 0]]

                for dr, dc in neighbours:
                    row = r+dr
                    col = c + dc
                    if min(row, col) < 0 or row == ROWS or col == COLS or heights[row][col] < heights[r][c]  or (row, col) in visited_pac:
                        continue

                    dfs_pac(row, col, visited_pac)
                
                return

            for c in range(0, COLS):
                dfs_pac(0, c, visited_pac)
                dfs_atl(ROWS-1, c, visited_atl)
            
            for r in range(0, ROWS):
                dfs_pac(r, 0, visited_pac)
                dfs_atl(r, COLS-1, visited_atl)
            
            print(visited_atl)
            print(visited_pac)
            for r in range(ROWS):
                for c in range(COLS):
                    if (r, c) in visited_atl and (r, c) in visited_pac:
                        res.append([r,c])
            
            return res        