class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        max_sum = float("-inf")
        temp_sum = 0
        while i < len(nums):
            temp_sum += nums[i]
            
            max_sum = max(max_sum, temp_sum)

            if temp_sum < 0:
                temp_sum = 0
            
            i+=1

        return max_sum
