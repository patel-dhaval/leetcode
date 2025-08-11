class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0,0
        max_len = float("-inf")
        char_dict = {}

        for R in range(len(s)):
            char_dict[s[R]] = char_dict.get(s[R], 0) + 1            
            while (R-L+1 - max(char_dict.values())) > k:
                    char_dict[s[L]] -= 1
                    L += 1
            max_len = max(max_len, R - L + 1)

        return max_len