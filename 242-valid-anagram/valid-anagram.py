class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif len(s) == 1 and len(t) == 1:
            if s == t:
                return True
            return False
        
        freq_arr = [0] * 26

        for i in range(len(s)):
            freq_arr[ord(s[i]) - ord('a')] += 1
            freq_arr[ord(t[i]) - ord('a')] -= 1
        
        for i in freq_arr:
            if i != 0:
                return False
        
        return True