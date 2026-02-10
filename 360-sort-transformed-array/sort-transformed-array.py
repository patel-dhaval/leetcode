"""
Dry Run:
nums = [-4,-2,2,4], a = 1, b = 3, c = 5
index_ptr = 3,2,1,0
val_l = 3
val_r = 3
res = [3,9,15,33]
"""

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
            n = len(nums)
            res = [0] * n
            index_ptr = 0

            if a >= 0:
                index_ptr = len(nums) - 1
            
            l = 0
            r = len(nums) - 1

            while l <= r:
                val_l = a * (nums[l] * nums[l]) + b * nums[l] + c
                val_r = a * (nums[r] * nums[r]) + b * nums[r] + c

                if a>=0:
                    if val_l > val_r:
                        res[index_ptr] = val_l
                        l+=1
                    else:
                        res[index_ptr] = val_r
                        r-=1
                    index_ptr -= 1
                else:
                    if val_l > val_r:
                        res[index_ptr] = val_r
                        r-=1
                    else:
                        res[index_ptr] = val_l
                        l+=1
                    index_ptr += 1
            
            return res