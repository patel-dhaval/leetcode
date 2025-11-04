class Solution:
    def isAlpha(self, s: str) -> bool:
        if s.isdigit() or ord(s.lower()) in range(ord('a'), ord('z')):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while not self.isAlpha(s[L]) and L < R:
                L+=1
            while not self.isAlpha(s[R]) and L < R:
                R -= 1
            if s[L].lower() == s[R].lower():
                L += 1
                R -= 1
            else:
                return False
        return True
            