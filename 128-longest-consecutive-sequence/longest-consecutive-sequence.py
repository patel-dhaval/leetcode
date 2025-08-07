class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        count = 0
        for i in set_nums:
            if (i - 1) in set_nums:
                continue
            else:
                count = 1
                while i + count in set_nums:
                    count += 1
                max_count = max(count, max_count)
        
        return max_count

                
