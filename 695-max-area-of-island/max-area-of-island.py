class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        maxSum = 0

        def dfs(r,c) -> int:
            visited.add((r,c))
            row, col = r,c
            directions= [[1,0],[-1,0],[0,1],[0,-1]]
            sum = 1
            for dr,dc in directions:
                r,c = row + dr, col + dc
                if (r) in range(rows) and (c) in range(cols) and grid[r][c] == 1 and (r ,c) not in visited:
                    sum += dfs(r, c)
            return sum

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxSum = max(dfs(r,c), maxSum)

        return maxSum

        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # maxSum = 0

        # def dfs(r, c) -> int:
        #     visited.add((r, c))
        #     sum = 1
        #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #     for dr, dc in directions:
        #         nr, nc = r + dr, c + dc
        #         if (nr) in range(rows) and (nc) in range(cols) and grid[nr][nc] == 1 and (nr, nc) not in visited:
        #             sum += dfs(nr, nc)  # Add the result of recursive dfs call to the current sum
        #     return sum

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r, c) not in visited:
        #             maxSum = max(dfs(r, c), maxSum)

        # return maxSum