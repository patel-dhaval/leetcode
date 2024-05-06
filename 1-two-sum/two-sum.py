class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(0, len(nums)):
            num_2 = target - nums[i]
            if num_2 in hmap:
                return([i, hmap[num_2]])
            else:
                hmap[nums[i]] = i
