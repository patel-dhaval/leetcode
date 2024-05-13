class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hmap = {')': '(', '}':'{', ']':'[' }

        for c in s:
            if c not in hmap:
                stk.append(c)
                continue
            if not stk or stk[-1] != hmap[c]:
                return False
            stk.pop()

        return not stk
        