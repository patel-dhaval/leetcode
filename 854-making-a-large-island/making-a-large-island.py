class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_area = collections.defaultdict(int)
        current_id = 2
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c, current_id):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] != 1:
                return 0
            
            grid[r][c] = current_id
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc, current_id)
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c, current_id)
                    island_area[current_id] = area
                    current_id += 1
        
        if not island_area:
            if grid[0][0] == 0:
                return 1
        
        max_area = max(island_area.values())

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    neighbour_ids = set()
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == 0:
                            continue
                        neighbour_ids.add(grid[nr][nc])
                    
                    current_flag_len = 1

                    for id in neighbour_ids:
                        current_flag_len += island_area[id]

                    max_area = max(max_area, current_flag_len)

        return max_area