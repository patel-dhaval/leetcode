class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        i = 0

        while i < len(nums):
            if target - nums[i] in hmap:
                return [i, hmap[target - nums[i]]]
            else:
                hmap[nums[i]] =  i
            i+=1
            # print(hmap)

