class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_len = float("inf")
        total_sum = 0
        for r in range(len(nums)):
            total_sum += nums[r]
            while total_sum >= target:
                min_len = min(min_len, r - l + 1)
                total_sum -= nums[l]
                l+=1
        
        return min_len if min_len != float('inf') else 0