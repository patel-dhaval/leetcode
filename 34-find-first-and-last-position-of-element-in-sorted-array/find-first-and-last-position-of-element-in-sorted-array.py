class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(first_position):
            low = 0
            high = len(nums) - 1

            
            ans = -1
            while low <= high:
                mid = (low + high)//2
                if target == nums[mid]:
                    ans = mid
                    
                    if first_position:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return ans


        return [search(1), search(0)]

