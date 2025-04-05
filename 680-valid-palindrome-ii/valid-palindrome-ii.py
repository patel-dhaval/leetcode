class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validP(s):
            reverse = s[::-1]
            if s == reverse:
                return True

        l, r = 0 , len(s)-1
        count = 1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            elif count > 0:
                count -= 1
                if validP(s[l:r]):
                    r -=1
                elif validP(s[l+1:r+1]):
                    l+=1
            else:
                return False
        return True
