"""
Approach: For 2 strings to be anagrams, they need to have the exact combination of characters. 
Thus, using a frequency array would be good. 
Instead of using 2 freq arrays and then comparing, we can use just 1, adding 1 to the existing value if the char is in s and subtracting 1 if the value is in t. 
Once all the input is processed, check freq array, if any non-zero element found then not anagrams, else anagrams
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freq_arr = [0] * 26

        for i in range(len(s)):
            freq_arr[ord(s[i]) - ord('a')] +=1
            freq_arr[ord(t[i]) - ord('a')] -=1
        
        for i in freq_arr:
            if i != 0:
                return False
        return True