class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")
        if len(prices) < 2:
            return 0
        
        L, R = 0, 1

        while R in range(1, len(prices)):
            if prices[L] < prices[R]:
                max_profit = max(max_profit, prices[R] - prices[L])
            else:
                L = R
            R+=1
            
        return max_profit if max_profit != float("-inf") else 0