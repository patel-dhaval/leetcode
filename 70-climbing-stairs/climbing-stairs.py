# class Solution:
#     def climbStairs(self, n: int) -> int:
#         cache = [-1] * n

#         def dfs(i):
#             if i >= n:
#                 return i == n
#             if cache[i] != -1:
#                 return cache[i]
            
#             cache[i] = dfs(i+1) + dfs(i+2)

#             return cache[i]
        
#         return dfs(0)


# Python3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]