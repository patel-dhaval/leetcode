class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        fresh, rotten = 0, 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten += 1
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        if rotten == 0:
            return -1

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                visit.add((r,c))
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1

            if fresh == 0:
                return time
        return -1
