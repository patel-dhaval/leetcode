class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) < 1:
        #     return 0
        # visited_set = set()
        # L = 0
        # max_len = 1
        # visited_set.add(s[L])
        # for R in range(1, len(s)):
        #     while s[R] in visited_set:
        #         visited_set.remove(s[L])
        #         L += 1
        #     visited_set.add(s[R])
        #     max_len = max(max_len, len(visited_set))


        # return max_len

        L = 0
        visited = set()
        max_count = 0
        for R in range(len(s)):
            if s[R] not in visited:
                visited.add(s[R])
                max_count = max(max_count, len(visited))
            else:
                while s[R] in visited:
                    visited.remove(s[L])
                    L+=1
                visited.add(s[R])
        return max_count