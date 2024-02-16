class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = 0
        res = []
        i = 0 
        hmap = {}

        while i <= len(nums)-1:
            check = target - nums[i]
            if check in hmap:
                return [i,hmap[check]]
            else:
                hmap[nums[i]] = i
            i +=1