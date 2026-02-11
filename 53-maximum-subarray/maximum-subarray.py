"""
DRY RUN:
nums = [-2, 1, -3, 4,-1,2,1,-5]
curr_sum = 1
max_sum = 6
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]
        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        
        return max_sum