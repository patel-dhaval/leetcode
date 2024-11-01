class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        visit = set()
        length = 0

        if grid[0][0] == 1 or grid[(rows -1)][(cols-1)] == 1:
            return -1

        directions = [[0,1],[0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        queue.append((0, 0))
        visit.add((0,0))
        length +=1

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                
                if row == rows-1 and col == cols - 1:
                    return length

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if min(r, c) < 0 or r >= rows or c >= cols or (r, c) in visit or grid[r][c] != 0:
                        continue
                    queue.append((r,c))
                    visit.add((r,c))
            length +=1
        
        return -1
