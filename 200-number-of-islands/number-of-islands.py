class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        number_of_islands = 0

        def dfs(r,c):
            visited.add((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == '0' or (nr, nc) in visited:
                    continue
                
                dfs(nr, nc)
        
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r, c)
                    number_of_islands += 1

        return number_of_islands