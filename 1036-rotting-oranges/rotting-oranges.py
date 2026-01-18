class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        rotten_oranges = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
                    rotten_oranges += 1

        if fresh_oranges == 0:
            return 0

        if rotten_oranges == 0:
            return -1

        neighbours = [[1,0], [-1, 0], [0, 1], [0, -1]] 
        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbours:
                    row = r + dr
                    col = c + dc

                    if min(row, col) < 0 or row == ROWS or col == COLS or grid[row][col] == 0 or grid[row][col] == 2:
                        continue
                    
                    grid[row][col] = 2
                    queue.append((row, col))
                    fresh_oranges -= 1
            
            time += 1
            if fresh_oranges == 0:
                return time
        return -1
