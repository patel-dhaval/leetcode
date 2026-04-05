class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(low, high, direction):
            ans = -1

            while low <= high:
                mid = (low + high)//2

                if nums[mid] == target:
                    ans = mid

                    if direction:
                        high = mid - 1
                    else:
                        low = mid + 1
                
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return ans
        
        return [search(0, len(nums)-1, 1),search(0, len(nums)-1, 0)]


