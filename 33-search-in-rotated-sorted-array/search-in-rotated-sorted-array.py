"""
l = 0, 4
nums[l] = 4, 0
r = 6
nums[r] = 2
mid = 3, 5
nums[mid] = 7, 1

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if target == nums[mid]:
                return mid

            elif nums[mid] > nums[r]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
