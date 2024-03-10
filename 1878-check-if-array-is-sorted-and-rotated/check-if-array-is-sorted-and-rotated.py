class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True

        # Find the rotation point (breakpoint)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                # Found a decrease, indicating rotation
                break
        else:
            # No rotation point found, array is already sorted
            return True

        # Check if the rotated array matches the sorted version
        rotated_array = nums[i:] + nums[:i]
        sorted_array = sorted(nums)
        return rotated_array == sorted_array