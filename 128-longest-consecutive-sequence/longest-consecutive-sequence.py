class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


#Logic is to find the start of sequence, which should not have a left neighbour elements, eg if sequence starts with 1 then it would not have 0 in the set. once found, check for the length of the sequence checking it against the set and adding it to the length, append the max value of this length to the longest and that should be the answer. Set lookup will be in O(n) and memory for the set would be O(n)