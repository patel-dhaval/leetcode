"""
Clarifying questions

Edge cases

Approach

Code

TC

SC

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        L , R = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while L  <  R :
            mid = L + (R - L ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[R]:
                L = mid + 1
                
            # left has the  min 
            else:
                R = mid - 1 
                
        return min(curr_min,nums[L])