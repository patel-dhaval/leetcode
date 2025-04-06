class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_vol = 0
        while l < r:
            vol = min(height[l], height[r]) * (r - l)
            max_vol = max(vol, max_vol)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_vol