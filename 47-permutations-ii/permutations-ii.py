class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        
        if idx == len(nums):
            self.res.append(nums[:])
            return
        processed_ip = set()
        for i in range(idx, len(nums)):
            if nums[i] not in processed_ip:
                processed_ip.add(nums[i])
                nums[idx], nums[i] = nums[i], nums[idx]
                self.backtrack(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]