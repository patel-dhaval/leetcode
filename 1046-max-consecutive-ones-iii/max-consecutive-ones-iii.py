"""
DRY RUN:
zero_count = 3
idx = 5
jdx = 10
res = 6
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        zero_count = 0
        idx = 0
        res = 0

        for jdx in range(n):
            if nums[jdx] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[idx] == 0:
                    zero_count -= 1
                
                idx += 1
            
            res = max(res, jdx - idx + 1)
        
        return res
