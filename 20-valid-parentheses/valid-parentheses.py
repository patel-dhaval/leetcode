class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {'}': '{', ')':'(', ']':'['}
        stack = []

        if len(s) < 2:
            return False
        
        for i in range(len(s)):
            if s[i] not in bracketMap:
                stack.append(s[i])
            elif s[i] in bracketMap and stack:
                top = stack.pop()
                if bracketMap[s[i]] != top:
                    return False
            else:
                return False
            
            
        if not stack:
            return True
        else:
            return False
          