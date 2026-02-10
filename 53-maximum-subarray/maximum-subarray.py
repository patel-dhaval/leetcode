class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[r]
            max_sum = max(curr_sum, max_sum)
        
        return max_sum
            