"""
ip: 4 5 6 7 0 1 2, tgt = 0
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) -1 

        

        while l <= r:
            
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            ## Left Sorted
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                   
            #Right sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
            

