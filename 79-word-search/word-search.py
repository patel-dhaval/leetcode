class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r, c, idx):
            
            if (r,c) in visited:
                return False

            if idx == len(word) -1:
                return True

            index = idx+1

            visited.add((r, c))

            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                row = r + dr
                col = c + dc 

                if 0 <= row < ROWS and 0 <= col < COLS and index < len(word) and board[row][col] == word[index] and (row, col) not in visited:
                    if dfs(row, col, index):
                        return True
                
            visited.remove((r,c))

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r, c, 0):
                        return True
        
        return False
        


