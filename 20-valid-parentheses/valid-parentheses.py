class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        para_map = {"}": "{", ")":"(", "]":'['}
        stack = []
        for c in s:
            if c in para_map.values():
                stack.append(c)
            else:
                if stack and stack[-1] == para_map[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
