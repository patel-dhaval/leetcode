class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0
        rotten_oranges = 0
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        queue = collections.deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    rotten_oranges += 1
                    queue.append((r,c))
        
        if fresh_oranges == 0:
            return 0

        if rotten_oranges == 0:
            return -1
        time = 0        
        while queue:
            for _ in range(len(queue)):
                r, c  =  queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue

                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr, nc))
                    if fresh_oranges == 0:
                        return time + 1
            time += 1
        
        return time if fresh_oranges == 0 else -1


