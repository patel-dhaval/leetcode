class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Approach: Use Binary sesarch to identify which half the min would be located
        This will be done by comparing the middle element with left and right most element.
        If the middle is greater than the left element, there is still no clarity if its in first or second half, so we compare with right as well, and if the mid is smaller then the right element, that means its in the first half, else second half.
        Similarly, if the element is smaller than the left element, we still need to further check with the right element, if the mid is greater right element then its in the second half, else its first half
        """

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[left]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
        return nums[left] 

        