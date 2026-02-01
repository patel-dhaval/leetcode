class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        temp_count = 0
        for n in nums:            
            if n == 1:
                temp_count += 1
            else:
                max_count = max(max_count, temp_count)
                temp_count = 0
        max_count = max(max_count, temp_count)
        return max_count