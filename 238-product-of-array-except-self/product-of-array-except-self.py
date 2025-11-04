class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_val = 1
        postfix_val = 1
        res = []
        res.append(prefix_val)
        for n in nums[:len(nums)-1]:
            res.append(prefix_val * n)
            prefix_val = prefix_val * n
        for r in range(len(res)-1, -1, -1):
            res[r] =  res[r] * postfix_val
            postfix_val = postfix_val * nums[r]
        
        return res
