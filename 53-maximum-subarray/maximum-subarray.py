class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sum = 0

        for i in range(len(nums)):

            sum += nums[i]

            if sum > maxi:
                maxi = sum

            # If sum < 0: discard the sum calculated
            if sum < 0:
                sum = 0

        return maxi