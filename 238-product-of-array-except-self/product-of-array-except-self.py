class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = []
        res.append(prefix)
        for i in range(len(nums)-1):
           res.append(prefix * nums[i])
           prefix = prefix * nums[i]

        postfix = 1

        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j] * postfix
            postfix = postfix * nums[j]
        
        return res