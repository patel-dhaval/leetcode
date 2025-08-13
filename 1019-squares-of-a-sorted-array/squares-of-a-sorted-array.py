class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # left, right = 0, len(nums) -1
        # while left < right:
        #     if nums[right]**2 < nums[left]**2:
        #         nums[right], nums[left] = nums[left],nums[right]
        #     right -= 1

        return sorted((list(x**2 for x in nums)))