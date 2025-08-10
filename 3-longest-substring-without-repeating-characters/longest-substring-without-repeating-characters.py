class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_len = 1
        result_set = set()
        L, R = 0, 0
        result_set.add(s[L])
        for R in range(1, len(s)):
            if s[R] not in result_set:
                result_set.add(s[R])
                max_len = max(len(result_set), max_len)
            else:
                while s[R] in result_set:
                    result_set.remove(s[L])
                    L += 1
                result_set.add(s[R])
        return max_len