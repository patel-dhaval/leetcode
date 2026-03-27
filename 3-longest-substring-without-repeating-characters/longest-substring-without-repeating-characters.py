class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 0:
            return 0

        char_set = set()
        i = 0
        max_len = 0

        for j in range(len(s)):
            if s[j] in char_set:
                while char_set and s[j] in char_set:
                    char_set.remove(s[i])
                    i += 1
            
            char_set.add(s[j])
            max_len = max(max_len, j - i + 1)
            
        return max_len