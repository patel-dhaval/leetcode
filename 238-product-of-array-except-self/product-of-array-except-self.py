"""
Approach:
precomputation
prefix and postfix multiplication
using temp as 1 for both instances
Left to right, we start building the res arr
Right to left, we update the res array values

TC: O(n)
SC: O(1) if res not included
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_arr = [1 for _ in range(len(nums))] 
        temp = 1
        for i in range(1, len(nums)):
            res_arr[i] = temp * nums[i-1]
            temp = temp * nums[i-1]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            res_arr[i] = temp * res_arr[i]
            temp =  temp * nums[i]

        return res_arr

        