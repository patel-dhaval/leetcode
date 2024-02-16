class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap_row = collections.defaultdict(set)
        hmap_col = collections.defaultdict(set)
        hmap_3x3 = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue

                if (board[row][col] in hmap_row[row] or
                board[row][col] in hmap_col[col] or
                board[row][col] in hmap_3x3[(row//3, col//3 )]):
                    return False

                hmap_col[col].add(board[row][col])
                hmap_row[row].add(board[row][col])
                hmap_3x3[(row // 3, col // 3)].add(board[row][col])
                
        return True