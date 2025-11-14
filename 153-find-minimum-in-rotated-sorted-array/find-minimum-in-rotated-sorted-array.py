class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L+R)//2
            if nums[mid] > nums[L]:
                if nums[mid] > nums[R]:
                    L = mid + 1
                else:
                    R = mid
            else:
                if nums[mid] < nums[R]:
                    R = mid
                else:
                    L = mid + 1
        return nums[L]