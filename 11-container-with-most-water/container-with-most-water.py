"""
Approach
2 pointers
move the pointer which has the smaller value
compute volume (min-height) * distance
return max_volume
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        L, R = 0, len(height) - 1

        while L < R:
            volume = min(height[L], height[R]) * (R - L)
            max_volume = max(max_volume, volume)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return max_volume