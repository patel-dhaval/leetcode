class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(combination, openB, closeB):
            if openB == closeB == n:
                temp = "".join(combination.copy())
                res.append(temp)
            
            if openB < n:
                combination.append("(")
                backtrack(combination, openB +1 , closeB)
                combination.pop()
            
            if closeB < openB:
                combination.append(")")
                backtrack(combination, openB, closeB + 1)
                combination.pop()
            
        
        backtrack([], 0, 0)
        return res