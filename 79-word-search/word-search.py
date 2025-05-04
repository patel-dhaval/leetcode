class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def word_seach(r, c, idx):
            if (r,c) in visit:
                return False
            
            if idx == len(word) -1:
                return True

            visit.add((r,c))
            
            directions = [[1,0], [-1, 0], [0,1], [0,-1]]

            for dr, dc in directions:
                row = r + dr
                col = c + dc
                next_index = idx + 1
                if min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visit or next_index >= len(word) or board[row][col] != word[next_index]:
                    continue
                if word_seach(row, col, next_index):
                    return True
            
            visit.remove((r,c))
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visit = set()
                    if word_seach(r,c,0):
                        return True
        return False
