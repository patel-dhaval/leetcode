class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixVal, postfixVal = 1, 1
        soln = []

        for i in range(len(nums)):
            soln.append(prefixVal)
            prefixVal = prefixVal * nums[i]
        print(soln)
        for i in range(len(nums)-1, -1, -1):
            soln[i] = postfixVal * soln[i]
            postfixVal = postfixVal * nums[i]
        return soln

