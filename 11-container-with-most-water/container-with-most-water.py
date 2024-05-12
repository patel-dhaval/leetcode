class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        maxVol = 0

        while r > l:
            vol = min(height[r],height[l]) * (r-l)
            if vol > maxVol:
                maxVol = vol
            # print(maxVol)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxVol

