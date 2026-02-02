class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_count = 0
        i = 0
        temp_count = 0
        max_count = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            
            max_count = max(max_count, j - i + 1)

        return max_count
                

