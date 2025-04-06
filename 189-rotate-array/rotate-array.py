class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1

        k = k % len(nums)

        nums.reverse()
        
        reverse(0, k-1, nums)
        reverse(k, len(nums)-1, nums)