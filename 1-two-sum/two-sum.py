class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed_nums = {}

        for i,n in enumerate(nums):
            if (target - n) in processed_nums.keys():
                return [i, processed_nums[(target - n)]]
            else:
                processed_nums[n] = i
