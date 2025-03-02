# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         if not grid or not grid[0]:
#             return -1

#         ROWS = len(grid)
#         COLS = len(grid[0])
#         fresh_oranges = 0
#         queue = collections.deque()


#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == 1:
#                     fresh_oranges += 1
#                 elif grid[r][c] == 2:
#                     queue.append((r,c))
        
#         if fresh_oranges == 0:
#             return 0

#         directions = [[1,0], [0, -1], [1, 0], [0, -1]]
#         time = 0

#         while queue:
#             time +=1
#             for _ in range(len(queue)):
#                 r, c = queue.popleft()
#                 for dr, dc in directions:
#                     row = r + dr
#                     col = c + dc

#                     if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
#                         grid[row][col] = 2
#                         queue.append((row, col))
#                         fresh_oranges -= 1

#             if fresh_oranges == 0:
#                 return time            

          
#         return -1


import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = collections.deque()

        # Count fresh oranges and add rotten oranges to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        # If there are no fresh oranges, no time is needed
        if fresh_oranges == 0:
            return 0

        # Directions: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0

        # BFS traversal
        while queue:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh_oranges -= 1

            if fresh_oranges == 0:
                return time

        return -1
