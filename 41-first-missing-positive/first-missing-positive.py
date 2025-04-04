import sys
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_int = int(sys.maxsize)
        for i in range(1, max_int):
            if i in nums:
                continue
            else:
                return i