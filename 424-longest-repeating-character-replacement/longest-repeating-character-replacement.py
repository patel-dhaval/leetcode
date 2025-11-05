class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L= 0
        char_counts = {}
        max_len = 1
        for R in range(len(s)):
            if s[R] in char_counts:
                char_counts[s[R]] += 1
            else:
                char_counts[s[R]] = 1
            
            while (R-L+1 - max(char_counts.values())) > k:
                char_counts[s[L]] -= 1
                L += 1
            max_len = max(max_len, (R-L+1))

        return max_len