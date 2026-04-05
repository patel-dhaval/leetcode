"""
DRY RUN:
ip = [7, 0, 1,2,3, 4]
target= 2

low = 3
high = 5

mid = 4
nums[mid] = 3
 
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return mid
                
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            

        return -1