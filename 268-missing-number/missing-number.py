class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = (n*(n+1))//2

        sum_list = 0

        for i in nums:
            sum_list += i
        
        return sum_n - sum_list