"""
ip = [1,2,-1,-3, 4]
curr_sum = 4
max_sum = 4
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for idx in range(1, len(nums)):
            curr_sum = max(0, curr_sum)
            curr_sum += nums[idx]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum