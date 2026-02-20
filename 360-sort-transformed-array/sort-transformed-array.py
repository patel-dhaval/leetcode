"""
DRY RUN:

nums = [-4,-2,2,4], a = 1, b = 3, c = 5

res = [3,9,15,33]
index_ptr = 3
l = 1
r = 1
val_1 = 9
val_2 = 33

"""
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        """
        since the equation is a parabola, the a value here would control the direction, and the max value would lie on one of the extremes.
        If a is positive, then the max value would be present on the right extreme, else if a is negative then the smallest value would be on the left most side.
        """

        res = [0] * len(nums)
        
        if a>=0:
            index_ptr = len(nums) - 1
        else:
            index_ptr = 0

        l = 0
        r = len(nums) -1

        while l <= r:
            val_1 = a * (nums[l]**2) + b * nums[l] + c
            val_2 = a * (nums[r]**2) + b * nums[r] + c

            if a>=0:
                if val_1 > val_2:
                    res[index_ptr] = val_1
                    l += 1
                else:
                    res[index_ptr] = val_2
                    r -= 1
                index_ptr -= 1
            else:
                if val_1 < val_2:
                    res[index_ptr] = val_1
                    l += 1
                else:
                    res[index_ptr] = val_2
                    r -= 1
                index_ptr += 1
        
        return res