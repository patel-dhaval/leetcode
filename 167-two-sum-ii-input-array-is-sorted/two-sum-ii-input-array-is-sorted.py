class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        nums = numbers
        for i in range(len(nums)):
            sum = target - nums[i]
            print(hmap)
            if sum not in hmap:
                hmap[nums[i]] = i
            else:
                soln = [hmap[sum]+1, i+1]
                return soln
        