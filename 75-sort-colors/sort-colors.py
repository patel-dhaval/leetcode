"""
Approach:
use low, mid and high

if ip == 0: swap low with mid, and increment both low and mid
if ip == 1: increment mid
if ip == 2: swap with mid and decement high

constraint is that mid <= high
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low +=1
                mid +=1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
