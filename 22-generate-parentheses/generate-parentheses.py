class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN, closeN = 0, 0
        res = []

        def dfs(temp, openN, closeN):
            if openN == n and closeN == n:
                res.append(temp)
            
            if openN < n:
                temp1 = temp + '('
                dfs(temp1, openN+1, closeN)
            
            if closeN < openN:
                temp1 = temp + ')'
                dfs(temp1, openN, closeN+1)
            
            return temp

        dfs('', 0, 0)

        return res

