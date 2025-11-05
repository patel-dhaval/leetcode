class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for R in range(1, len(prices)):
            if prices[R] > prices[R-1]:
                profit = prices[R] - prices[R-1]
                max_profit += profit
        return max_profit