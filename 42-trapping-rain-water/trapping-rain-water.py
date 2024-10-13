class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        maxWater = 0
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(height[l], maxLeft)
                maxWater += (maxLeft - height[l])

            else:
                r -=1
                maxRight = max(height[r], maxRight)
                maxWater += (maxRight - height[r])
        
        return maxWater