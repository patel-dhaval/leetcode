class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        comp = []
        for i in range(n+1):
            comp.append(i)
        
        for i in comp:
            if i not in nums:
                return i