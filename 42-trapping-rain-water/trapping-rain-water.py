"""
Clarifying questions
Before the first and the last input, are we considering that the elevation is zero?
Only positive Heights considered


Edge Cases
First and Last positions will never hold any water if the 0th and the last + 1 positions are at zero elevation

Approach
We would use two pointers. Tracking of the max Left and the max Right values
At every position, we will calculate how much water can be stored - water : min(maxL, maxR) - height
if height > 0, add, else, 0
move either L or R depending on whichever is smaller
Keep processing till l < r
Once this condition breaks, we know that we have successfully processed all input and we will have the solution

Algo

Dry Run


TC


Sc


"""


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