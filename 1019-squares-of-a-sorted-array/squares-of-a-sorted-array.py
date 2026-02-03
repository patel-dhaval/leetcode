class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        index_ptr = n - 1
        l, r = 0, n -1
        while l <= r:
            l_val = nums[l] * nums[l]
            r_val = nums[r] * nums[r]

            max_val = max(l_val, r_val)

            res[index_ptr] = max_val
            index_ptr -= 1
            if l_val > r_val:
                l += 1
            else:
                r -=1
        
        return res