"""
Approach:
use two pointer
use helper functions to identify alphanumeric
use string functions to convert to lowercase and compare
if l > r and no mismatch, return True, else return False
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1

        while L < R:
            if s[L].isalnum() and s[R].isalnum():
                if s[L].lower() == s[R].lower():
                    L += 1
                    R -=1
                    continue
                else:
                    return False
            elif not s[L].isalnum():
                L +=1
            elif not s[R].isalnum():
                R -= 1
        return True
