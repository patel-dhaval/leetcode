from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def dfs(r, c):
            # Use DFS to mark cells connected to the boundary as visited
            if (r, c) in visited or board[r][c] != 'O':
                return
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)
        
        # Mark all 'O's connected to the boundary as visited
        for r in range(rows):
            for c in [0, cols - 1]:  # left and right columns
                if board[r][c] == 'O':
                    dfs(r, c)
        for c in range(cols):
            for r in [0, rows - 1]:  # top and bottom rows
                if board[r][c] == 'O':
                    dfs(r, c)
        
        # Flip all 'O's that are not visited to 'X' and convert visited back to 'O'
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'
                elif (r, c) in visited:
                    board[r][c] = 'O'
