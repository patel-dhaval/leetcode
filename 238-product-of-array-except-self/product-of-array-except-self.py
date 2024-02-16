class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = 1
        pre = 1
        op = [1] * len(nums)

        for i in range(0, len(nums)):
                op[i] = pre
                pre = pre * nums[i]

        for i in range(len(nums)-1, -1, -1):
            op[i] = post * op[i]
            post = post * nums[i]

        return(op)