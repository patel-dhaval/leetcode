class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        i, j = 0, 1
        maxProfit = 0

        while j < len(prices) and i < len(prices) - 1:
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)
                j+=1
            else:
                i = j
                j = i + 1
            
        return maxProfit