class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN, closeN = 0, 0
        res = []
        val_stack = []
        
        def backtrack(openN, closeN):
            if openN == n and closeN == n:
                res.append("".join(val_stack))
            
            if openN < n:
                val_stack.append('(')
                backtrack(openN+1, closeN)
                val_stack.pop()
            
            if closeN < openN:
                val_stack.append(')')
                backtrack(openN, closeN+1)
                val_stack.pop()

        backtrack(0, 0)

        return res

