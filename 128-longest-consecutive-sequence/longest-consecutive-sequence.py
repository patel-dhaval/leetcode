class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup_set = set(nums)
        max_len = 0
        for i in lookup_set:
            if i-1 not in lookup_set:
                length = 1
                while i + length in lookup_set:
                    length += 1
                max_len = max(max_len, length)

        return max_len