class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_vol = 0
        while L < R:
            volume = min(height[L], height[R]) * (R - L)
            max_vol = max(max_vol, volume)
            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        return max_vol
