from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_count = len(heights)
        col_count = len(heights[0])
        res = []
        visited_atl = set()
        visited_pac = set()

        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]


        def dfs_atl(r, c):
            visited_atl.add((r, c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < row_count and
                    0 <= col < col_count and
                    heights[row][col] >= heights[r][c] and
                    (row, col) not in visited_atl):
                    dfs_atl(row, col)

        def dfs_pac(r, c):
            visited_pac.add((r, c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < row_count and
                    0 <= col < col_count and
                    heights[row][col] >= heights[r][c] and
                    (row, col) not in visited_pac):
                    dfs_pac(row, col)

        for c in range(col_count):
            dfs_pac(0, c)
            dfs_atl(row_count - 1, c)

        for r in range(row_count):
            dfs_pac(r, 0)
            dfs_atl(r, col_count - 1) 

        for r in range(row_count):
            for c in range(col_count):
                if (r, c) in visited_atl and (r, c) in visited_pac:
                    res.append([r, c])

        return res
