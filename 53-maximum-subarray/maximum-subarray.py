class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        max_sum = nums[0]
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[r]
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                l = r
            else:
                r += 1
        
        return max_sum
            