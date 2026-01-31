class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(findFirst):
            ans = -1
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    if findFirst:
                        high = mid - 1 # Keep looking left
                    else:
                        low = mid + 1  # Keep looking right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        
        start_value = search(1)
        end_value = search(0)

        return [start_value, end_value]