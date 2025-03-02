from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        ROWS, COLS = len(rooms), len(rooms[0])
        queue = deque()

        # Add all gates (0s) to the queue first
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist = 0
        
        while queue:
            dist += 1  # Increment distance once per BFS layer
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Skip if out of bounds or if it's a wall (-1) or already closer to a gate
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or rooms[row][col] != 2147483647:
                        continue
                    
                    # Update distance and add to queue
                    rooms[row][col] = dist
                    queue.append((row, col))
