class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(0, nums)
        return self.res
    
    def backtrack(self, idx, nums):
        if idx == len(nums) - 1:
            self.res.append(nums[:])

        for jdx in range(idx, len(nums)):
            nums[idx], nums[jdx] = nums[jdx], nums[idx]
            self.backtrack(idx+1, nums)
            nums[idx], nums[jdx] = nums[jdx], nums[idx]