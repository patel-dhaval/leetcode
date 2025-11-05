class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0
        for R in range(1, len(prices)):
            profit = prices[R] - prices[L]
            max_profit = max(max_profit, profit)
            if prices[R] < prices[L]:
                L = R
        return max_profit
