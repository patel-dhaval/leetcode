'''
Prefix & Postfix on the input arr to calculate product of arr except self

Prefix

inialize prefix factor to 1
Set first position as 1
carry out operation and update the prefix factor
proceed till length of prefix == input

Posfix:

initialize the factor to 1
Carry out operation from end of the input till the start
Update the factor by mulitplying with the input at that curr position

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1

        res = []

        for i in range(0 , len(nums)):
            res.append(pre)
            pre = pre * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]
        
        return res