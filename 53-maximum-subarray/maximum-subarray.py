class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = 0
        max_sum = nums[0]
        curr_sum = 0
        for R in range(len(nums)):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[R]
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                L = R
        return max_sum