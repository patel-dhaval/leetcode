class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Calculate the effective rotation steps (to handle cases where k is    larger than the array length)
        k = k % len(nums)
        
        # Reverse the entire array
        # reverse(nums, 0, len(nums) - 1)
        nums.reverse()
        
        # Reverse the first k elements
        reverse(nums, 0, k - 1)
        
        # Reverse the remaining elements
        reverse(nums, k, len(nums) - 1)

def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1