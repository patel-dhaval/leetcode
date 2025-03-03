import collections
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        queue = collections.deque()

        # Add all 'O's on the border to the queue
        for r in range(ROWS):
            if board[r][0] == "O":
                queue.append((r, 0))
            if board[r][COLS - 1] == "O":
                queue.append((r, COLS - 1))

        for c in range(COLS):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[ROWS - 1][c] == "O":
                queue.append((ROWS - 1, c))

        # BFS and mark connected 'O's as 'T' (temporary)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            r, c = queue.popleft()
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O":
                board[r][c] = "T"  # Temporarily mark it
                for dr, dc in directions:
                    queue.append((r + dr, c + dc))

        # Flip remaining 'O' to 'X', and 'T' back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
