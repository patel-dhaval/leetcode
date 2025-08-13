class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # Suboptimal solution
        # return sorted((list(x**2 for x in nums)))
        
        res = [0 for _ in range(len(nums))]

        i, left, right = len(nums) - 1, 0, len(nums) - 1

        while i >= 0:
            if nums[right]**2 > nums[left]**2:
                res[i] = nums[right]**2
                right -= 1
            else:
                res[i] = nums[left]**2
                left += 1
            i-=1
        return res
