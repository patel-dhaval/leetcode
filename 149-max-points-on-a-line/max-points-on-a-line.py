"""
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
max_points = 3
p1 = [3,2]
p2 = [4,1]
dy = -1
dx = 1
slope_map = {-1: 3, 0.5: 1, 1:1, 2:1, inf: 1}

points = [[1,1], [1,1], [1,1]]
max_points = 3
p1 = [1,1]
p2 = [1,1]
dy = 0
dx = 0
slope_map = {inf: 3}

"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n
        
        max_points = 0

        for idx in range(n):
            p1 = points[idx]

            slope_map = collections.defaultdict(int)

            for jdx in range(idx+1, n):
                p2 = points[jdx]

                dy = p2[1] - p1[1]
                dx = p2[0] - p1[0]

                if dx == 0:
                    slope = float("inf")
                else:
                    slope = dy/dx

                slope_map[slope] += 1
            
                max_points = max(max_points, slope_map[slope]+1)
        

        return max_points