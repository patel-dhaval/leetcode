class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        queue = collections.deque()
        directions = [[0,1], [0, -1], [1,0], [-1, 0]]

        fresh_orange = False

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 1:
                    fresh_orange = True
        
        if not fresh_orange:
            return 0

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
        
        while queue:
            r, c, time = queue.popleft()
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (row < row_count and 
                    row >= 0 and
                    col < col_count and
                    col >= 0 and
                    grid[row][col] == 1):

                    grid[row][col] = 2

                    queue.append((row, col, time + 1))
        
        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 1:
                    return -1
        
        return time

