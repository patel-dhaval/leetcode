class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return n
        
        ans = 1
        
        for i in range(n):
            slope_map = collections.defaultdict(int)
            p1 = points[i]
            
            for j in range(i + 1, n):
                p2 = points[j]
                
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                
                # Handle Vertical Line (dx is 0)
                if dx == 0:
                    slope = "inf"
                else:
                    # Reduce fraction using GCD
                    # common = math.gcd(dy, dx)
                    slope = dy/dx
                
                slope_map[slope] += 1
                ans = max(ans, slope_map[slope] + 1) # +1 includes the anchor point itself
                
        return ans