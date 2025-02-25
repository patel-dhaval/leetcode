'''
Approach
2 Pointers, calc volume - dist * min(heights1, heights2)
if h1 < h2:
    h1 +=1
else:
    h2 -= 1
keep tracking max volume 
break condiiton when h1 > h2

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        maxVol = 0
        while L < R:
            vol = (R - L) * min(height[L], height[R])
            maxVol = max(vol, maxVol)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxVol