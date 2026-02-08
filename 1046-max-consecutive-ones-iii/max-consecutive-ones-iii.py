class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        zero_count = 0
        max_ones = 0

        for j in range(len(nums)):
            if nums[j] == 1:
                max_ones = max(max_ones, j-i+1)

            elif nums[j] == 0:
                zero_count += 1

                while zero_count > k:
                    if nums[i] == 0:
                        zero_count -= 1
                    i += 1
        
            max_ones = max(max_ones, j-i+1)
        
        return max_ones

